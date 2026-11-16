from fastapi.testclient import TestClient
from app.main import app
c=TestClient(app)
def test_catalogue():
 assert len(c.get("/indicators").json())==3
 assert len(c.get("/indicators/immunization_coverage").json()["observations"])==3
def test_summary_and_unknown():
 r=c.get("/regions/summary?indicator=immunization_coverage").json()
 assert r["mean"]==89.5 and r["min"]==87.5
 assert c.get("/indicators/unknown").status_code==404
def test_quality():
 r=c.get("/data-quality").json(); assert r["dataset"]=="synthetic" and r["completeness_percent"]==100
