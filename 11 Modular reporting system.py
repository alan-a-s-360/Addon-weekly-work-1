# modular reporting system 11
def sales_report():
    print("Sales Report Generated")


def inventory_report():
    print("Inventory Report Generated")


def employee_report():
    print("Employee Report Generated")


def generate_report(report_type):
    reports = {
        "sales": sales_report,
        "inventory": inventory_report,
        "employee": employee_report
    }

    if report_type in reports:
        reports[report_type]()
    else:
        print("Invalid report type")


# Example usage
generate_report("sales")
generate_report("inventory")
generate_report("employee")
