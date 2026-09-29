# VISHWANATH Cafe Management System

A simple Python-based console application for taking a cafe order and calculating the bill. The project was developed as a beginner-level implementation of a cafe ordering workflow using Python concepts such as dictionaries, variables, input/output, conditional statements and arithmetic operations.

## 1. Project Overview

The **VISHWANATH Cafe Management System** allows a customer to:

1. View the cafe menu.

2. Enter the name of an item to order.

3. Check whether the entered item is available.

4. Add an item if required.

5. Calculate the price of the selected items.

6. Display the amount and a thank-you message.

The current implementation is a *console-based application** and does not use a database, graphical user interface, web framework or external Python libraries.

## 2. Problem Statement

In a cafe manually noting customer orders and calculating the bill can lead to unnecessary effort and calculation mistakes. A simple computerized ordering program can make the process easier by displaying the menu validating whether an item is available accepting customer choices and calculating the amount automatically.

This project implements a solution to that problem using Python.

## 3. Objectives

The main objectives of the project are:

- To create a digital cafe ordering system.

- To display a predefined menu with item prices.

- To accept customer input through the console.

- To validate ordered items against the menu.

- To calculate the total price automatically.

- To provide clear feedback when an item is unavailable.

- To demonstrate the use of basic Python programming concepts in a real-world context.

## 4. Functional Requirements

The project currently provides the following modules:

### Module 1: Menu Management / Menu Display

A Python dictionary stores the available menu items and their prices.

Current menu items include:

| Item | Price (Rs.) |

|---|---:|

| Sandwich | 80 |

Red sauce pasta | 85 |

| White sauce pasta | 100

| Veg Burger | 80 |

Farmhouse pizza | 130 |

| Garlic Bread | 95 |

Paneer buteer masala | 180 |

| Paneer lababdar | 195 |

| Kadhai Paneer | 150 |

| Shahi Paneer | 160 |

Chicken butter masala | 210 |

### Module 2: Order Input and Validation

The program asks the customer for the first item.

If the entered item exists in the menu its price is added to the order total. A confirmation message is displayed.

If the item is not present in the menu the program informs the customer that the item's unavailable.

The program then asks whether the customer wants to add another item and if the answer is `Yes` accepts and validates an item.

### Module 3: Bill Calculation and Output

The variable `order_total` starts at zero.

For each selected item the corresponding price from the menu dictionary is added to `order_total`.

At the end the program displays the amount that the customer has to pay.

## 5. Input and Output

### Inputs

The application accepts:

- Name of the food item.

- `Yes` or `No` response for adding another item.

- Name of the second food item when the customer chooses `Yes`.

### Outputs

The application displays:

- message.

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

v

Initialize order_total = 0

|

v

Enter First Item

+---- Item available? ---- Yes ----> Add price to total

|                                      |

v

|                              Ask for another item

|

No

v

Display "Item not available"

|

v

Ask for another item

|

+---- Yes ----> Enter Second Item

|

|                   +---- Available? ---- Yes ----> Add price

|                   |                               |

|                   |                               v

|                   |                       Display total

|                   |

|                   No

|

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

- **Python Concepts:** Dictionary variables, input/output, `if-else`, arithmetic operations, membership checking, f-strings

- **External Libraries:** None

- **Database:** None

- **Interface:** Command-line / console

- **Version Control:** Git/GitHub can be used for repository management

## 8. Requirements

To run the project you need:

- Python 3.x

- A code editor or IDE such as VS Code, PyCharm, IDLE or another Python-supported editor

- A terminal/command prompt

No third-party Python packages are required.

## 9. Installation

### Step 1: Install Python

Install Python 3.x on your computer.

Verify the installation:

```bash

python --version

```

On some systems use:

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

If your final repository uses an entry-point file replace `main.py` with that filename.

## 10. Example Usage

A typical interaction is:

```text

Welcome to VISHWANATH Cafe

Here is the menu for the day

[menu is displayed]

Enter the name of item you want to order = Sandwich

Your item Sandwich has been added to your order

Do you want to add another item? (Yes/No) Yes

Enter the name of item = Garlic Bread

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

### Test Case 1: first item

**Input:**

```text

Sandwich

No

```

**Expected result:**

```text

The total amount of items to pay is 80

```

### Test Case 2: Two items

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

### Test Case 3: Invalid item

**Input:**

```text

French Fries

No

```

**Expected behavior:**

The program should display that the ordered item is not available and the total remains `0`.

### Test Case 4: first item and invalid second item

**Input:**

```text

Sandwich

Yes

French Fries

```

**Expected result:**

The first item is added the second item is rejected as unavailable and the final total remains `80`.

### Test Case 5: No item

**Input:**

```text

Pizza item from the displayed menu

No

```

**Expected behavior:**

the valid first items price is included in the final total.

## 12. Error Handling

The current implementation performs validation by checking whether the entered item exists in the menu dictionary.

For example:

```python

if item_1 in menu:

```

If the item is not present the program displays an unavailable-item message of adding an invalid price.

The current version does not yet handle every invalid input, such as different capitalization (`sandwich` instead of `Sandwich`) or invalid responses other than `Yes`/`No`.

## 13. Non-Functional Requirements

The project should satisfy the following -functional requirements:

### 13.1 Usability

The console interaction should be simple enough for a user to understand the menu enter an item and see the final bill, without technical knowledge.

### 13.2 Performance

For the predefined menu item lookup and total calculation should complete immediately during normal use.

### 13.3 Reliability

The system should work consistently without crashing. It should not give totals or allow invalid inputs to affect the final bill. The program should handle each case correctly. Give proper feedback to the user.

The system must not include an item in the total if that item is not available in the menu. Basic item validation is already in place.

### 13.4 Maintainability

Menu prices are stored in a dictionary, which allows for updates to individual menu items. However the current codebase has duplicated sections across files. This repetition reduces maintainability. Makes future changes more difficult. Refactoring the code will improve clarity. Make it easier to manage.

### 13.5 Error Handling

Invalid menu items are. Rejected during input. While this prevents selections the current validation is limited. Future versions can benefit from input checks to handle edge cases and improve robustness.

## 14. Project Structure

The uploaded project includes these Python files:

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

**Important:** The current version of the Python files contains a lot of repeated code. In the GitHub submission the files should be refactored so each file handles one clear responsibility. Avoid having copies of the same logic.

## 15. Recommended Modular Structure

The VITyarthi guidelines require coding and suggest at least five to ten meaningful modules or classes.

A better structure for the version could look like this:

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

The new files should contain real functionality or actual tests not just be added to reach a certain number of files.

## 16. Design Overview

The logical flow of the system is as follows:

```text

+----------------------+

Customer       |

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

The current implementation is minimal. Designed for simplicity. It has limitations:

- Users can select only up to two items at a time.

- There is no order history saved between sessions.

- No database is used to store menu or order data.

- There is no graphical user interface.

- A printable bill is not generated separately.

- Quantity selection for each item is missing.

- Taxes and discounts are not calculated.

- No user accounts or login system exists.

- Code duplication appears across the files.

- Input matching is case-sensitive so "Coffee" and "coffee" are treated differently.

- Automated unit testing has not been implemented yet.

These shortcomings can be addressed in updates.

## 18. Future Enhancements

Possible improvements include:

1. Allow ordering than two items.

2. Add quantity selection for each menu item.

3. Automatically calculate subtotal, tax, discount and final bill.

4. Improve input validation to handle typos and incorrect entries.

5. Make item searches case-insensitive.

6. Store customer and order records separately.

7. Keep an order history for users.

8. Use SQLite or another database to store data.

9. Create a graphical user interface.

10. Implement automated unit tests.

11. Generate printed receipts.

12. Improve separation by organizing code into distinct files.

## 19. Academic Compliance Note

The VITyarthi project guidelines require requirements at least four non-functional requirements, proper design documentation, modular implementation, error handling, testing where needed version control using Git and complete GitHub documentation.

This README describes the *current implementation as submitted**. Some of the required elements—such, as having meaningful modules UML diagrams, automated tests and clean modular structure—are not fully met by the current code. These aspects need to be added or improved before the submission.

## 20. References

- VITyarthi – Build Your Project: General Project Instructions & Submission Guidelines.

- Python 3 documentation and course material used during development.


