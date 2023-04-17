// This is a read operation on 'admin' database

DB = db.getSiblingDB('admin');
DB.system.version.find();
