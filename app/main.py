from fastapi import FastAPI,HTTPException,Query
app=FastAPI(title="Public Health Intelligence Dashboard",version="1.0.0")
IND={
"immunization_coverage":{"name":"Immunization coverage","unit":"percent","definition":"Share of eligible children reported fully immunized."},
"reported_tb_rate":{"name":"Reported TB rate","unit":"per_100k","definition":"Reported tuberculosis cases per 100,000 population."},
"maternal_care_4plus":{"name":"Four or more antenatal visits","unit":"percent","definition":"Share of recorded pregnancies with at least four antenatal visits."}}
# Fictional values for software demonstration only.
ROWS=[
{"region":"North","indicator":"immunization_coverage","value":91.2,"year":2025},
{"region":"South","indicator":"immunization_coverage","value":87.5,"year":2025},
{"region":"East","indicator":"immunization_coverage","value":89.8,"year":2025},
{"region":"North","indicator":"reported_tb_rate","value":112.0,"year":2025},
{"region":"South","indicator":"reported_tb_rate","value":98.0,"year":2025},
{"region":"East","indicator":"reported_tb_rate","value":125.0,"year":2025},
{"region":"North","indicator":"maternal_care_4plus","value":78.0,"year":2025},
{"region":"South","indicator":"maternal_care_4plus","value":83.0,"year":2025}]
@app.get("/health")
def health(): return {"status":"ok","dataset":"synthetic","records":len(ROWS)}
@app.get("/indicators")
def indicators(): return [{"code":k,**v} for k,v in IND.items()]
@app.get("/indicators/{code}")
def indicator(code:str):
 if code not in IND: raise HTTPException(404,"Unknown indicator code")
 return {"code":code,**IND[code],"observations":[r for r in ROWS if r["indicator"]==code]}
@app.get("/regions/summary")
def summary(indicator:str=Query(min_length=2)):
 if indicator not in IND: raise HTTPException(404,"Unknown indicator code")
 rows=[r for r in ROWS if r["indicator"]==indicator]; vals=[r["value"] for r in rows]
 return {"indicator":indicator,"unit":IND[indicator]["unit"],"observations":rows,"mean":round(sum(vals)/len(vals),2),"min":min(vals),"max":max(vals)}
@app.get("/data-quality")
def quality():
 n=len(ROWS); complete=sum(r.get("value") is not None for r in ROWS)
 return {"dataset":"synthetic","total_records":n,"complete_records":complete,"completeness_percent":round(complete/n*100,2),"missing_values":n-complete,"note":"Completeness does not establish accuracy or comparability."}
