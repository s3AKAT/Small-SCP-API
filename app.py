from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/scp", methods=['GET'])
def get_scp():
    scp = [
        {
            "id": 1,
            "marked": "SCP-001",
            "name": "Pending Declassification",
            "description": "The information has been deleted...",
            "class": "Not assigned or neutralized",
        },
        
        {
            "id": 2,
            "marked": "SCP-002",
            "name": "Living Room",
            "description": "SCP-002 resembles a fleshy tumor with a volume of approximately 60 m3. On one side there is an iron hatch that leads inside the facility. The interior is a standard cheap room of small size. There is a window on one of the walls that is not visible from the outside. There is furniture in the room, which, as can be found out after a closer examination, is made of bones, hair and other biological substances that the human body produces. All studies have shown that the DNA of individual things does not match or is fragmented.",
            "class": "Euclid",
        },
        
        {
            "id": 3,
            "marked": "SCP-003",
            "name": "Biological Motherboard",
            "description": "SCP-003 consists of two interconnected objects of different origins, which are further designated as SCP-003-1 and SCP-003-2.",
            "class": "Euclid",
        },
        
                {
            "id": 4,
            "marked": "SCP-004",
            "name": "12 Rusty Keys and a Door",
            "description": "SCP-004 consists of an old wooden barn door (SCP-004-1) and a bunch of twelve rusty steel keys (SCP-004-2 - SCP-004-13). The door itself is the entrance to an abandoned factory in [DATA DELETED].",
            "class": "Euclid",
        },
        
        {
            "id": 5,
            "marked": "SCP-005",
            "name": "Skeleton Key",
            "description": "SCP-005 looks like an ornate key, which does not differ in characteristics from commercially available keys of the 1920s. The key was discovered when a civilian used it when entering a specially protected facility. Apparently, SCP-005 has a unique ability to open all types of locks without much difficulty (see Appendix A), both mechanical and electronic. The origin of this feature has not been established at the moment.",
            "class": "Safe",
        },
    ]
    return jsonify(scp)

if __name__ == "__main__":
    app.run(debug=True)
    
    
    
    
    