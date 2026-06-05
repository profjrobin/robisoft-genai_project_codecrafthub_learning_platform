from flask import Flask, request, jsonify
import json
import os
from datetime import datetime

app = Flask(__name__)

DATA_FILE = "courses.json"

VALID_STATUSES = ["Not Started", "In Progress", "Completed"]

REQUIRED_FIELDS = ["name", "description", "target_date", "status"]


# Create courses.json automatically if it does not exist
def initialize_data_file():
    if not os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "w") as file:
                json.dump([], file, indent=4)
        except IOError:
            print("Error: Could not create courses.json")


# Load course data from the JSON file
def load_courses():
    try:
        initialize_data_file()

        with open(DATA_FILE, "r") as file:
            return json.load(file)

    except (IOError, json.JSONDecodeError):
        raise Exception("Unable to read course data file")


# Save course data to the JSON file
def save_courses(courses):
    try:
        with open(DATA_FILE, "w") as file:
            json.dump(courses, file, indent=4)

    except IOError:
        raise Exception("Unable to write course data file")


# Check date format: YYYY-MM-DD
def is_valid_date(date_text):
    try:
        datetime.strptime(date_text, "%Y-%m-%d")
        return True
    except ValueError:
        return False


# Validate required fields and business rules
def validate_course_data(data):
    for field in REQUIRED_FIELDS:
        if field not in data or not data[field]:
            return f"Missing required field: {field}"

    if not is_valid_date(data["target_date"]):
        return "target_date must be in YYYY-MM-DD format"

    if data["status"] not in VALID_STATUSES:
        return "Invalid status. Must be: Not Started, In Progress, or Completed"

    return None


# Generate the next course ID
def get_next_id(courses):
    if not courses:
        return 1

    return max(course["id"] for course in courses) + 1


@app.route("/courses", methods=["GET"])
def get_courses():
    try:
        courses = load_courses()
        return jsonify(courses), 200

    except Exception as error:
        return jsonify({"error": str(error)}), 500


@app.route("/courses/<int:course_id>", methods=["GET"])
def get_course(course_id):
    try:
        courses = load_courses()

        for course in courses:
            if course["id"] == course_id:
                return jsonify(course), 200

        return jsonify({"error": "Course not found"}), 404

    except Exception as error:
        return jsonify({"error": str(error)}), 500


@app.route("/courses", methods=["POST"])
def create_course():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "Request body must be valid JSON"}), 400

        validation_error = validate_course_data(data)

        if validation_error:
            return jsonify({"error": validation_error}), 400

        courses = load_courses()

        new_course = {
            "id": get_next_id(courses),
            "name": data["name"],
            "description": data["description"],
            "target_date": data["target_date"],
            "status": data["status"],
            "created_at": datetime.now().isoformat()
        }

        courses.append(new_course)
        save_courses(courses)

        return jsonify(new_course), 201

    except Exception as error:
        return jsonify({"error": str(error)}), 500


@app.route("/courses/<int:course_id>", methods=["PUT"])
def update_course(course_id):
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "Request body must be valid JSON"}), 400

        validation_error = validate_course_data(data)

        if validation_error:
            return jsonify({"error": validation_error}), 400

        courses = load_courses()

        for course in courses:
            if course["id"] == course_id:
                course["name"] = data["name"]
                course["description"] = data["description"]
                course["target_date"] = data["target_date"]
                course["status"] = data["status"]

                save_courses(courses)

                return jsonify(course), 200

        return jsonify({"error": "Course not found"}), 404

    except Exception as error:
        return jsonify({"error": str(error)}), 500


@app.route("/courses/<int:course_id>", methods=["DELETE"])
def delete_course(course_id):
    try:
        courses = load_courses()

        updated_courses = [
            course for course in courses if course["id"] != course_id
        ]

        if len(updated_courses) == len(courses):
            return jsonify({"error": "Course not found"}), 404

        save_courses(updated_courses)

        return jsonify({"message": "Course deleted successfully"}), 200

    except Exception as error:
        return jsonify({"error": str(error)}), 500


# Start the Flask development server
if __name__ == "__main__":
    initialize_data_file()
    app.run(debug=True)