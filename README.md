# VISHWANATH Cafe Management System

A simple Python-based console application for taking a cafe order and calculating the total bill. The project was developed as a beginner-level implementation of a cafe ordering workflow using core Python concepts such as dictionaries, variables, input/output, conditional statements, and arithmetic operations.

## 1. Project Overview

The **VISHWANATH Cafe Management System** allows a customer to:

1. View the available cafe menu.
2. Enter the name of an item to order.
3. Check whether the entered item is available.
4. Add a second item if required.
5. Calculate the total price of the selected items.
6. Display the final amount and a thank-you message.

The current implementation is a **console-based application** and does not use a database, graphical user interface, web framework, or external Python libraries.

## 2. Problem Statement

In a small cafe, manually noting customer orders and calculating the bill can lead to unnecessary effort and calculation mistakes. A simple computerized ordering program can make the process easier by displaying the menu, validating whether an item is available, accepting customer choices, and calculating the total amount automatically.

This project implements a basic solution to that problem using Python.

## 3. Objectives

The main objectives of the project are:

- To create a simple digital cafe ordering system.
- To display a predefined menu with item prices.
- To accept customer input through the console.
- To validate ordered items against the available menu.
- To calculate the total price automatically.
- To provide clear feedback when an item is unavailable.
- To demonstrate the use of basic Python programming concepts in a real-world context.

## 4. Functional Requirements

The project currently provides the following functional modules:

### Module 1: Menu Management / Menu Display

A Python dictionary stores the available menu items and their prices.

Current menu items include:

| Item | Price (Rs.) |
|---|---:|
| Sandwich | 80 |
| Red sauce pasta | 85 |
| White sauce pasta | 100 |
| Veg Burger | 80 |
| Farmhouse pizza | 130 |
| Garlic Bread | 95 |
| Paneer buteer masala | 180 |
| Paneer lababdar | 195 |
| Kadhai Paneer | 150 |
| Shahi Paneer | 160 |
| Chicken butter masala | 210 |

### Module 2: Order Input and Validation

The program asks the customer for the first item.

If the entered item exists in the menu, its price is added to the order total and a confirmation message is displayed.

If the item is not present in the menu, the program informs the customer that the item is unavailable.

The program then asks whether the customer wants to add another item and, if the answer is `Yes`, accepts and validates a second item.

### Module 3: Bill Calculation and Output

The variable `order_total` starts at zero.

For each valid selected item, the corresponding price from the menu dictionary is added to `order_total`.

At the end, the program displays the total amount that the customer has to pay.

## 5. Input and Output

### Inputs

The application accepts:

- Name of the first food item.
- `Yes` or `No` response for adding another item.
- Name of the second food item when the customer chooses `Yes`.

### Outputs

The application displays:

- Welcome message.
- Available menu.
- Item-added confirmation.
- Item-unavailable message when applicable.
- Final total amount.
- Thank-you message.

## 6. Project Workflow

```text
Start
  |
  v
Display Welcome Message
  |
  v
Display Menu
  |
  v
Initialize order_total = 0
  |
  v
Enter First Item
  |
  +---- Item available? ---- Yes ----> Add price to total
  |                                      |
  |                                      v
  |                              Ask for another item
  |
  No
  |
  v
Display "Item not available"
  |
  v
Ask for another item
  |
  +---- Yes ----> Enter Second Item
  |                   |
  |                   +---- Available? ---- Yes ----> Add price
  |                   |                               |
  |                   |                               v
  |                   |                       Display final total
  |                   |
  |                   No
  |                   |
  |                   v
  |             Display unavailable message
  |
  No
  |
  v
Display final total
  |
  v
Thank You
  |
  v
End
```

## 7. Technologies and Tools Used

- **Programming Language:** Python
- **Python Concepts:** Dictionary, variables, input/output, `if-else`, arithmetic operations, membership checking, f-strings
- **External Libraries:** None
- **Database:** None
- **Interface:** Command-line / console
- **Version Control:** Git/GitHub can be used for repository management

## 8. Requirements

To run the project, you need:

- Python 3.x
- A code editor or IDE such as VS Code, PyCharm, IDLE, or another Python-supported editor
- A terminal/command prompt

No third-party Python packages are required.

## 9. Installation

### Step 1: Install Python

Install Python 3.x on your computer.

Verify the installation:

```bash
python --version
```

On some systems, use:

```bash
python3 --version
```

### Step 2: Download or Clone the Repository

Clone the GitHub repository:

```bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
```

Then enter the project directory:

```bash
cd <PROJECT-DIRECTORY>
```

### Step 3: Run the Program

The main executable file should be:

```bash
python main.py
```

If your final repository uses a different entry-point file, replace `main.py` with that filename.

## 10. Example Usage

A typical interaction is:

```text
Welcome to VISHWANATH Cafe
Here is the menu for the day
[menu is displayed]

Enter the name of item you want to order = Sandwich
Your item Sandwich has been added to your order

Do you want to add another item? (Yes/No) Yes

Enter the name of second item = Garlic Bread
Item Garlic Bread is has been added to order

The total amount of items to pay is 175
Thank You
Please visit again
```

For example:

```text
Sandwich = Rs. 80
Garlic Bread = Rs. 95

Total = Rs. 175
```

## 11. Testing Instructions

The current program can be tested manually using the following cases.

### Test Case 1: Valid first item

**Input:**
```text
Sandwich
No
```

**Expected result:**
```text
The total amount of items to pay is 80
```

### Test Case 2: Two valid items

**Input:**
```text
Sandwich
Yes
Garlic Bread
```

**Expected result:**
```text
The total amount of items to pay is 175
```

### Test Case 3: Invalid first item

**Input:**
```text
French Fries
No
```

**Expected behavior:**

The program should display that the ordered item is not available and the total remains `0`.

### Test Case 4: Valid first item and invalid second item

**Input:**
```text
Sandwich
Yes
French Fries
```

**Expected result:**

The first item is added, the second item is rejected as unavailable, and the final total remains `80`.

### Test Case 5: No second item

**Input:**
```text
Pizza item from the displayed menu
No
```

**Expected behavior:**

Only the valid first item's price is included in the final total.

## 12. Error Handling

The current implementation performs basic validation by checking whether the entered item exists in the menu dictionary.

For example:

```python
if item_1 in menu:
```

If the item is not present, the program displays an unavailable-item message instead of adding an invalid price.

The current version does not yet handle every possible invalid input, such as different capitalization (`sandwich` instead of `Sandwich`) or invalid responses other than `Yes`/`No`.

## 13. Non-Functional Requirements

The project should satisfy the following non-functional requirements:

### 13.1 Usability

The console interaction should be simple enough for a user to understand the menu, enter an item, and see the final bill without technical knowledge.

### 13.2 Performance

For the small predefined menu, item lookup and total calculation should complete immediately during normal use.

### 13.3 Reliability

The system should not add an item to the total when that item is not present in the menu. Basic item validation is already implemented.

### 13.4 Maintainability

Menu prices are stored in a dictionary, which makes individual menu entries relatively easy to update. However, the current repository contains duplicated code across multiple files, so further refactoring is needed for better maintainability.

### 13.5 Error Handling

Invalid menu items are identified and rejected. More comprehensive input validation can be added in future versions.

## 14. Current Project Structure

The uploaded project currently contains these Python files:

```text
Project/
│
├── main.py
├── Menu.py
├── Order.py
├── Bill.py
├── README.md
└── statement.md
```

**Important:** The current uploaded Python files contain substantial duplicate code. In the final GitHub submission, the files should be refactored into clearly separated responsibilities instead of keeping multiple copies of the same program.

## 15. Recommended Modular Structure

The VITyarthi guidelines specify modular implementation and, for coding projects, a minimum of 5–10 meaningful modules/classes/files.

A stronger final structure could be:

```text
VISHWANATH-Cafe/
│
├── main.py
├── Menu.py
├── Order.py
├── Bill.py
├── validation.py
├── test_menu.py
├── test_order.py
├── README.md
└── statement.md
```

The additional files should contain real functionality or tests rather than being created only to increase the file count.

## 16. Design Overview

The current logical architecture can be represented as:

```text
             +----------------------+
             |       Customer       |
             +----------+-----------+
                        |
                        v
             +----------------------+
             |    Menu Display      |
             +----------+-----------+
                        |
                        v
             +----------------------+
             | Order Input &        |
             | Item Validation      |
             +----------+-----------+
                        |
                        v
             +----------------------+
             |   Bill Calculation   |
             +----------+-----------+
                        |
                        v
             +----------------------+
             | Final Total / Output |
             +----------------------+
```

## 17. Limitations of the Current Version

The current implementation is intentionally simple and has several limitations:

- It supports a maximum of two item selections in the current flow.
- It does not maintain a persistent order history.
- It does not use a database.
- It does not provide a graphical user interface.
- It does not generate a separate printable bill.
- It does not support quantities for each item.
- It does not calculate taxes or discounts.
- It does not have user accounts or authentication.
- It has duplicated code across the currently uploaded files.
- Input matching is case-sensitive.
- Comprehensive automated unit testing has not yet been implemented.

These limitations can be addressed as future enhancements.

## 18. Future Enhancements

Possible improvements include:

1. Support for ordering more than two items.
2. Quantity selection for each item.
3. Automatic subtotal, tax, discount, and final bill calculation.
4. Better input validation.
5. Case-insensitive item searching.
6. Separate customer and order records.
7. Order history.
8. Database integration using SQLite or another database.
9. Graphical user interface.
10. Automated unit tests.
11. Receipt generation.
12. Better modularization of the source code.

## 19. Academic Compliance Note

The VITyarthi project guidelines require functional requirements, at least four non-functional requirements, appropriate design documentation, modular implementation, validation/error handling, testing where applicable, Git/version control, and specific GitHub documentation.

This README documents the **current implementation as uploaded**. Some guideline requirements, particularly the minimum 5–10 meaningful modules/files, UML/design diagrams, automated testing, and stronger modular separation, are not fully demonstrated by the current uploaded code and should be added/refactored before final submission.

## 20. References

- VITyarthi – Build Your Own Project: General Project Instructions & Submission Guidelines.
- Python 3 documentation and course material used while developing the project.



