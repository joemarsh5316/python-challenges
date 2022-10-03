keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]



print(dict(zip(keys, values)))



sampleDict = {
    "class":{
        "student":{
            "name":"Mike",
            "marks":{
                "physics":70,
                "history":80
            }
        }
    }
}



print(str(sampleDict["class"]["student"]["marks"]["history"]))


sampleDict2 = {
    "name": "kelly",
    "age":25,
    "salary": 8000,
    "city": "new york"

}

keysToRemove = ["name", "salary"]

sampleDict == sampleDict2
True 
