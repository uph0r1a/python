import sqlite3

DB = "files/student_info.db"


def get_connection():
    conn = sqlite3.connect(DB)
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


def create_database():
    with get_connection() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS Majors (
                MajorID INTEGER PRIMARY KEY,
                Name    TEXT NOT NULL
            );
        """
        )
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS Departments (
                DeptID INTEGER PRIMARY KEY,
                Name   TEXT NOT NULL
            );
        """
        )
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS Students (
                StudentID INTEGER PRIMARY KEY,
                Name      TEXT NOT NULL,
                MajorID   INTEGER,
                DeptID    INTEGER,
                FOREIGN KEY (MajorID) REFERENCES Majors(MajorID),
                FOREIGN KEY (DeptID)  REFERENCES Departments(DeptID)
            );
        """
        )
    print("Database 'student_info.db' ready.\n")


def pick_major(conn):
    """Show all majors and return the chosen MajorID, or None to cancel."""
    rows = conn.execute("SELECT MajorID, Name FROM Majors ORDER BY Name;").fetchall()
    if not rows:
        print("No majors available. Please add majors first.")
        return None
    print(f"\n  {'ID':<6} {'Major'}")
    print("  " + "-" * 28)
    for row in rows:
        print(f"  {row[0]:<6} {row[1]}")
    valid_ids = {row[0] for row in rows}
    while True:
        try:
            choice = int(input("  Select MajorID: ").strip())
            if choice in valid_ids:
                return choice
            print("  Invalid ID. Please choose from the list.")
        except ValueError:
            print("  Please enter a number.")


def pick_department(conn):
    """Show all departments and return the chosen DeptID, or None to cancel."""
    rows = conn.execute(
        "SELECT DeptID, Name FROM Departments ORDER BY Name;"
    ).fetchall()
    if not rows:
        print("No departments available. Please add departments first.")
        return None
    print(f"\n  {'ID':<6} {'Department'}")
    print("  " + "-" * 28)
    for row in rows:
        print(f"  {row[0]:<6} {row[1]}")
    valid_ids = {row[0] for row in rows}
    while True:
        try:
            choice = int(input("  Select DeptID: ").strip())
            if choice in valid_ids:
                return choice
            print("  Invalid ID. Please choose from the list.")
        except ValueError:
            print("  Please enter a number.")


def add_major():
    name = input("Enter major name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    with get_connection() as conn:
        conn.execute("INSERT INTO Majors (Name) VALUES (?);", (name,))
    print(f"Major '{name}' added successfully.")


def search_major():
    name = input("Enter major name to search: ").strip()
    with get_connection() as conn:
        rows = conn.execute(
            "SELECT MajorID, Name FROM Majors WHERE Name LIKE ?;", (f"%{name}%",)
        ).fetchall()
    if rows:
        print(f"\n  {'ID':<6} {'Name'}")
        print("  " + "-" * 28)
        for row in rows:
            print(f"  {row[0]:<6} {row[1]}")
    else:
        print("No majors found.")


def show_all_majors():
    with get_connection() as conn:
        rows = conn.execute(
            "SELECT MajorID, Name FROM Majors ORDER BY Name;"
        ).fetchall()
    if rows:
        print(f"\n  {'ID':<6} {'Name'}")
        print("  " + "-" * 28)
        for row in rows:
            print(f"  {row[0]:<6} {row[1]}")
    else:
        print("No majors found.")


def update_major():
    show_all_majors()
    try:
        major_id = int(input("\nEnter MajorID to update: ").strip())
    except ValueError:
        print("Invalid ID.")
        return
    new_name = input("Enter new name: ").strip()
    if not new_name:
        print("Name cannot be empty.")
        return
    with get_connection() as conn:
        cursor = conn.execute(
            "UPDATE Majors SET Name = ? WHERE MajorID = ?;", (new_name, major_id)
        )
    if cursor.rowcount:
        print("Major updated successfully.")
    else:
        print("Major not found.")


def delete_major():
    show_all_majors()
    try:
        major_id = int(input("\nEnter MajorID to delete: ").strip())
    except ValueError:
        print("Invalid ID.")
        return
    with get_connection() as conn:
        try:
            cursor = conn.execute("DELETE FROM Majors WHERE MajorID = ?;", (major_id,))
            if cursor.rowcount:
                print("Major deleted successfully.")
            else:
                print("Major not found.")
        except sqlite3.IntegrityError:
            print("Cannot delete: students are assigned to this major.")


def majors_menu():
    options = {
        "1": ("Add a new major", add_major),
        "2": ("Search for a major", search_major),
        "3": ("Update an existing major", update_major),
        "4": ("Delete an existing major", delete_major),
        "5": ("Show all majors", show_all_majors),
        "6": ("Back", None),
    }
    while True:
        print("\n===== Majors Menu =====")
        for key, (label, _) in options.items():
            print(f"  {key}. {label}")
        choice = input("Select an option: ").strip()
        if choice == "6":
            break
        elif choice in options:
            options[choice][1]()
        else:
            print("Invalid choice. Please try again.")


def add_department():
    name = input("Enter department name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    with get_connection() as conn:
        conn.execute("INSERT INTO Departments (Name) VALUES (?);", (name,))
    print(f"Department '{name}' added successfully.")


def search_department():
    name = input("Enter department name to search: ").strip()
    with get_connection() as conn:
        rows = conn.execute(
            "SELECT DeptID, Name FROM Departments WHERE Name LIKE ?;", (f"%{name}%",)
        ).fetchall()
    if rows:
        print(f"\n  {'ID':<6} {'Name'}")
        print("  " + "-" * 28)
        for row in rows:
            print(f"  {row[0]:<6} {row[1]}")
    else:
        print("No departments found.")


def show_all_departments():
    with get_connection() as conn:
        rows = conn.execute(
            "SELECT DeptID, Name FROM Departments ORDER BY Name;"
        ).fetchall()
    if rows:
        print(f"\n  {'ID':<6} {'Name'}")
        print("  " + "-" * 28)
        for row in rows:
            print(f"  {row[0]:<6} {row[1]}")
    else:
        print("No departments found.")


def update_department():
    show_all_departments()
    try:
        dept_id = int(input("\nEnter DeptID to update: ").strip())
    except ValueError:
        print("Invalid ID.")
        return
    new_name = input("Enter new name: ").strip()
    if not new_name:
        print("Name cannot be empty.")
        return
    with get_connection() as conn:
        cursor = conn.execute(
            "UPDATE Departments SET Name = ? WHERE DeptID = ?;", (new_name, dept_id)
        )
    if cursor.rowcount:
        print("Department updated successfully.")
    else:
        print("Department not found.")


def delete_department():
    show_all_departments()
    try:
        dept_id = int(input("\nEnter DeptID to delete: ").strip())
    except ValueError:
        print("Invalid ID.")
        return
    with get_connection() as conn:
        try:
            cursor = conn.execute(
                "DELETE FROM Departments WHERE DeptID = ?;", (dept_id,)
            )
            if cursor.rowcount:
                print("Department deleted successfully.")
            else:
                print("Department not found.")
        except sqlite3.IntegrityError:
            print("Cannot delete: students are enrolled in this department.")


def departments_menu():
    options = {
        "1": ("Add a new department", add_department),
        "2": ("Search for a department", search_department),
        "3": ("Update an existing department", update_department),
        "4": ("Delete an existing department", delete_department),
        "5": ("Show all departments", show_all_departments),
        "6": ("Back", None),
    }
    while True:
        print("\n===== Departments Menu =====")
        for key, (label, _) in options.items():
            print(f"  {key}. {label}")
        choice = input("Select an option: ").strip()
        if choice == "6":
            break
        elif choice in options:
            options[choice][1]()
        else:
            print("Invalid choice. Please try again.")


def _print_students(rows):
    if rows:
        print(f"\n  {'ID':<6} {'Name':<25} {'Major':<25} {'Department'}")
        print("  " + "-" * 73)
        for row in rows:
            print(f"  {row[0]:<6} {row[1]:<25} {row[2]:<25} {row[3]}")
    else:
        print("No students found.")


def add_student():
    name = input("Enter student name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    with get_connection() as conn:
        print("\n-- Select Major --")
        major_id = pick_major(conn)
        if major_id is None:
            return
        print("\n-- Select Department --")
        dept_id = pick_department(conn)
        if dept_id is None:
            return
        conn.execute(
            "INSERT INTO Students (Name, MajorID, DeptID) VALUES (?, ?, ?);",
            (name, major_id, dept_id),
        )
    print(f"Student '{name}' added successfully.")


def search_student():
    name = input("Enter student name to search: ").strip()
    with get_connection() as conn:
        rows = conn.execute(
            """
            SELECT s.StudentID, s.Name,
                   COALESCE(m.Name, 'N/A') AS Major,
                   COALESCE(d.Name, 'N/A') AS Department
            FROM Students s
            LEFT JOIN Majors      m ON s.MajorID = m.MajorID
            LEFT JOIN Departments d ON s.DeptID  = d.DeptID
            WHERE s.Name LIKE ?
            ORDER BY s.Name;
            """,
            (f"%{name}%",),
        ).fetchall()
    _print_students(rows)


def show_all_students():
    with get_connection() as conn:
        rows = conn.execute(
            """
            SELECT s.StudentID, s.Name,
                   COALESCE(m.Name, 'N/A') AS Major,
                   COALESCE(d.Name, 'N/A') AS Department
            FROM Students s
            LEFT JOIN Majors      m ON s.MajorID = m.MajorID
            LEFT JOIN Departments d ON s.DeptID  = d.DeptID
            ORDER BY s.Name;
            """
        ).fetchall()
    _print_students(rows)


def update_student():
    show_all_students()
    try:
        student_id = int(input("\nEnter StudentID to update: ").strip())
    except ValueError:
        print("Invalid ID.")
        return
    with get_connection() as conn:
        row = conn.execute(
            "SELECT Name, MajorID, DeptID FROM Students WHERE StudentID = ?;",
            (student_id,),
        ).fetchone()
        if not row:
            print("Student not found.")
            return
        print(f"\nCurrent name: {row[0]}")
        new_name = input("Enter new name (press Enter to keep current): ").strip()
        if not new_name:
            new_name = row[0]
        print("\n-- Select new Major --")
        major_id = pick_major(conn)
        if major_id is None:
            return
        print("\n-- Select new Department --")
        dept_id = pick_department(conn)
        if dept_id is None:
            return
        conn.execute(
            "UPDATE Students SET Name = ?, MajorID = ?, DeptID = ? WHERE StudentID = ?;",
            (new_name, major_id, dept_id, student_id),
        )
    print("Student updated successfully.")


def delete_student():
    show_all_students()
    try:
        student_id = int(input("\nEnter StudentID to delete: ").strip())
    except ValueError:
        print("Invalid ID.")
        return
    with get_connection() as conn:
        cursor = conn.execute(
            "DELETE FROM Students WHERE StudentID = ?;", (student_id,)
        )
    if cursor.rowcount:
        print("Student deleted successfully.")
    else:
        print("Student not found.")


def students_menu():
    options = {
        "1": ("Add a new student", add_student),
        "2": ("Search for a student", search_student),
        "3": ("Update an existing student", update_student),
        "4": ("Delete an existing student", delete_student),
        "5": ("Show all students", show_all_students),
        "6": ("Back", None),
    }
    while True:
        print("\n===== Students Menu =====")
        for key, (label, _) in options.items():
            print(f"  {key}. {label}")
        choice = input("Select an option: ").strip()
        if choice == "6":
            break
        elif choice in options:
            options[choice][1]()
        else:
            print("Invalid choice. Please try again.")


def main():
    create_database()

    options = {
        "1": ("Manage Majors", majors_menu),
        "2": ("Manage Departments", departments_menu),
        "3": ("Manage Students", students_menu),
        "4": ("Exit", None),
    }

    while True:
        print("\n=============================")
        print("  Student Info Database App  ")
        print("=============================")
        for key, (label, _) in options.items():
            print(f"  {key}. {label}")
        choice = input("Select an option: ").strip()
        if choice == "4":
            print("Goodbye!")
            break
        elif choice in options:
            options[choice][1]()
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
