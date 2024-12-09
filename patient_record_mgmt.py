import csv
import graphviz
from binary_search_tree import BinarySearchTree, Node


class PatientRecord :
    def __init__(self, patient_id, name, age, diagnosis, blood_pressure, pulse, body_temperature):

        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.diagnosis = diagnosis
        self.blood_pressure = blood_pressure
        self.pulse = pulse
        self.body_temperature = body_temperature

class PatientRecordManagementSystem:
    def __init__(self):
        """Initializes the management system with an empty BST."""
        self.bst = BinarySearchTree()
    
    def add_patient_record(self, patient_id, name, age, diagnosis, blood_pressure, pulse, body_temperature):
        """Adds a new patient record to the system."""
        record = PatientRecord(patient_id, name, age, diagnosis, blood_pressure, pulse, body_temperature)
        node = Node(patient_id, record)
        self.bst.insert(node)
    
    def search_patient_record(self, patient_id):
        """Searches for a patient record by ID."""
        result = self.bst.search(patient_id)
        if result:
            record = result.value
            print(f"Patient Found - ID: {record.patient_id}, Name: {record.name}, Age: {record.age}, "
                  f"Diagnosis: {record.diagnosis}, BP: {record.blood_pressure}, Pulse: {record.pulse}, "
                  f"Temperature: {record.body_temperature}")
            return record
        else:
            print(f"Patient ID {patient_id} not found.")
            return None

    def delete_patient_record(self, patient_id):
        """Deletes a patient record from the system."""
        if self.bst.search(patient_id):
            self.bst.remove(patient_id)
            print(f"Deleted Patient ID: {patient_id}")
        else:
            print(f"Patient ID {patient_id} not found. Cannot delete.")
    
    def display_all_records(self):
        """Displays all patient records using inorder traversal."""
        print("All Patient Records (Inorder Traversal):")
        self.bst.inorder_traversal(self.bst.root)

    def build_tree_from_csv(self, file_path):
        """Builds the BST from a CSV file."""
        try:
            with open(file_path, mode='r') as file:
                # Normalize headers to lowercase for uniform access
                csv_reader = csv.DictReader(file)
                csv_reader.fieldnames = [field.strip().lower() for field in csv_reader.fieldnames]
                
                for row in csv_reader:
                    self.add_patient_record(
                        int(row["patientid"]),  # Adjusted for lowercase "patientid"
                        row["name"],
                        int(row["age"]),
                        row["diagnosis"],
                        row["bloodpressure"],
                        int(row["pulse"]),
                        float(row["bodytemperature"])
                    )
                print("Tree built from CSV successfully.")
        except Exception as e:
            print(f"Error while reading CSV file: {e}")

    
    def visualize_tree(self, output_file="patient_records_tree"):
        """Visualizes the BST using Graphviz and saves the result to a file."""
        dot = graphviz.Digraph()
        self._add_nodes(dot, self.bst.root)
        dot.render(output_file, format="png", cleanup=True)
        print(f"Tree visualization saved as {output_file}.png")
    
    def _add_nodes(self, dot, node):
        """Recursively adds nodes and edges to the Graphviz tree."""
        if node:
            dot.node(str(node.key), f"{node.key}: {node.value.name}")
            if node.left:
                dot.edge(str(node.key), str(node.left.key))
                self._add_nodes(dot, node.left)
            if node.right:
                dot.edge(str(node.key), str(node.right.key))
                self._add_nodes(dot, node.right)