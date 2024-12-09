# Import necessary modules
from patient_record_mgmt import PatientRecordManagementSystem

# Initialize the PatientRecordManagementSystem
prms = PatientRecordManagementSystem()

# Build the BST from the CSV file
csv_file_path = "data/patient_records.csv"  # Replace with your actual CSV file path
prms.build_tree_from_csv(csv_file_path)

# Display all records after loading the CSV
print("\nAll Patient Records (Initial):")
prms.display_all_records()

# Visualize the initial tree
prms.visualize_tree(output_file="initial_patient_records_tree")

# Search for specific patient records (IDs: 2, 25, 47)
print("\nSearch for patient records with IDs 2, 25, and 47:")
prms.search_patient_record(2)
prms.search_patient_record(25)
prms.search_patient_record(47)

# Delete records (IDs: 3, 10, and 30)
print("\nDeleting records with IDs 3, 10, and 30...")
prms.delete_patient_record(3)
prms.delete_patient_record(10)
prms.delete_patient_record(30)

# Display all records after deletion
print("\nAll Patient Records (After Deletion):")
prms.display_all_records()

# Visualize the tree after deletion
prms.visualize_tree(output_file="after-deletion_patient_records_tree")

# Add new records to the BST
new_records = [
    (51, "Jacob Marley", 40, "Migraine", "120/80", 70, 37.0),
    (58, "Robert Shea", 55, "Back Pain", "130/85", 75, 36.8),
    (3, "Joan Smith", 33, "Anxiety", "115/75", 68, 37.1)
]

print("\nInserting new patient records:")
for record in new_records:
    prms.add_patient_record(*record)

# Display all records after insertion
print("\nAll Patient Records (After Insertion):")
prms.display_all_records()

# Visualize the tree after insertion
prms.visualize_tree(output_file="after-insertion_patient_records_tree")

# Perform and display tree traversals
print("\nAll Patient Records (Inorder Traversal):")
prms.bst.inorder_traversal(prms.bst.root)

print("\nAll Patient Records (Preorder Traversal):")
prms.bst.preorder_traversal(prms.bst.root)

print("\nAll Patient Records (Postorder Traversal):")
prms.bst.postorder_traversal(prms.bst.root)