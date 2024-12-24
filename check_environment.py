import sys
import pkg_resources
import mysql.connector


print("Python executable:", sys.executable)
print("Installed packages:")
for dist in pkg_resources.working_set:
    print(f"{dist.project_name} ({dist.version})")
    print("MySQL Connector imported successfully!")
