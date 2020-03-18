from flask import Flask, jsonify, make_response, request, flash, redirect, render_template, session, abort, send_file, \
    url_for
import pymongo
from datetime import datetime
import os
from flask_cors import CORS, cross_origin
import json

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
my_customers = mydb["customers"]


def create_customer(content):
    try:
        my_dict = {"_id": check_valid_phone_number(content['_id']), 'Name': check_fil_letter(content['Name']),
                   'Password': content['Password'], "registration Date": current_date()}
        if not my_dict["_id"]:
            return False
        if not my_dict["Name"]:
            return False
        my_customers.insert_one(my_dict)
        return True
    except:
        return False


def search_db(search, val, db):
    myquery = {search: val}
    mydoc = db.find(myquery)
    return mydoc


def check_fil_letter(val_text):
    for char in val_text:
        if not str(char).isalpha() and not char.isspace():
            return False
    return val_text


def check_valid_phone_number(val):
    val_num = check_fill_num(val)
    valid_format = ['050', '054', '052', '053', '051', '055', '058']
    if val_num:
        if len(val_num) == 10:
            if val_num[:3] in valid_format:
                return val_num
            return False
        return False
    return False


def check_fill_num(val_num):
    val_num = str(val_num)
    if val_num.isdigit():
        return val_num
    return False


def current_date():
    now = datetime.now()
    today = now.strftime("%d/%m/%Y")
    return today


def not_found():
    return make_response("Not Found", 401)


def not_auth():
    return make_response("Not Found", 401)
