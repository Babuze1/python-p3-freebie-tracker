#!/usr/bin/env python3
# Script goes here!
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Company, Dev, Freebie

engine = create_engine('sqlite:///freebies.db')
Session = sessionmaker(bind=engine)
session = Session()

company1 = Company(name="Company A", founding_year=2000)
company2 = Company(name="Company B", founding_year=1995)

dev1 = Dev(name="Dev 1")
dev2 = Dev(name="Dev 2")

freebie1 = Freebie(item_name="Item 1", value=100, dev=dev1, company=company1)
freebie2 = Freebie(item_name="Item 2", value=50, dev=dev1, company=company2)
freebie3 = Freebie(item_name="Item 3", value=75, dev=dev2, company=company1)

session.add_all([company1, company2, dev1, dev2, freebie1, freebie2, freebie3])

session.commit()