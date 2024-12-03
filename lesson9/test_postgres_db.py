from sqlalchemy import create_engine
from sqlalchemy.sql import text
from sqlalchemy import inspect

db_connection_string = 'postgresql://postgres:11082005@localhost:5432/QA'

subject_params = {
        'subject_id': 666,
        'subject_title': 'Alchemy'
    }


def test_db_connection():
    db = create_engine(db_connection_string)
    inspector = inspect(db)
    names = inspector.get_table_names()
    assert 'subject' in names


def test_select():
    db = create_engine(db_connection_string)
    result = db.execute("select * from subject").fetchall()
    assert len(result) > 0


def test_create_subject():
    db = create_engine(db_connection_string)
    sql = text("insert into subject (subject_id, subject_title) " +
               "values (:subject_id, :subject_title)")
    db.execute(sql, **subject_params)
    return subject_params['subject_id']


def test_update_subject():
    db = create_engine(db_connection_string)
    new_subject_title = {**subject_params, 'subject_title': 'Art of Khemia'}
    sql_update = text("update subject set subject_title = :subject_title " +
                      "where subject_id = :subject_id")
    db.execute(sql_update, **new_subject_title)


def test_delete_subject():
    db = create_engine(db_connection_string)
    subject_id = test_create_subject()
    sql = text("delete from subject where subject_id = :subject_id")
    db.execute(sql, subject_id=subject_id)
