from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:3001/")
db = client.meteor

def insert_problem(eng_sentence, kr_sentence):
    problem = {"question": kr_sentence, "answer": eng_sentence, \
                "last_time": None, "recall_level": 0, \
                "next_time": datetime.utcnow()}

    db.problem_list.insert_one(problem)

if __name__ == '__main__':
    with open('sentence.tsv','r') as in_file:
        for line in in_file:
            eng_sentence, kr_sentence = line.strip().split('\t')
            insert_problem(eng_sentence, kr_sentence)
