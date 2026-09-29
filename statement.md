# VISHWANATH Cafe Management System. Project Statement

## 1. Problem Statement

Small cafes need to record customer orders and calculate the amount accurately. When this process is performed manually entering orders and adding prices can require effort and may result in calculation mistakes.

The VISHWANATH Cafe Management System is a Python-based console application designed to provide a basic computerized ordering process. The application displays a predefined cafe menu accepts the customers selected item checks whether the item is available optionally accepts an item and calculates the total amount to be paid.

The project applies Python programming concepts to a practical real-world cafe ordering problem.

## 2. Scope of the Project

The scope of the project is limited to a basic console-based cafe ordering workflow.

The system currently covers:

- Displaying the cafe menu.

- Storing menu items and prices in a Python dictionary.

- Accepting a food-item choice from the customer.

- Checking whether the selected item exists in the menu.

- Adding the valid items price to the order total.

- Allowing the customer to select a second item.

- Validating the item.

- Calculating and displaying the final order total.

- Displaying basic confirmation and unavailable-item messages.

The current version does not include database storage, customer accounts, online ordering, payment processing, graphical user interface, inventory management or persistent order history.

## 3. Target Users

The intended users of the system are:

### Primary Target User

Cafe customers

Customers can use the console interface to view items, select food items and see the amount to be paid.

### Secondary Target User

Cafe staff / small cafe operators

The project demonstrates how a simple computerized ordering workflow could reduce price calculation and basic order-entry effort.

### Academic User

Students and instructors

The project can also be used to demonstrate the application of Python programming concepts to a real-world problem.

## 4. High-Level Features

### 4.1 Menu Display

The system displays the cafe items and their prices.

The current menu contains items such as:

- Sandwich

- sauce pasta

- White sauce pasta

- Veg Burger

- Farmhouse pizza

- Garlic Bread

- Paneer buteer masala

- Paneer lababdar

- Kadhai Paneer

- Shahi Paneer

- Chicken butter masala

### 4.2 Item Selection

The customer enters the name of the item they want to order.

### 4.3 Item Availability Validation

The entered item is checked against the menu dictionary.

If the item is available its price is added to the order total.

If it is not available the system displays an unavailable-item message.

### 4.4 Multiple Item Ordering

The current program asks whether the customer wants to add another item. If the answer is Yes a second item can be. Validated.

### 4.5 Automatic Bill Calculation

The system maintains a value and adds the prices of valid selected items.

### 4.6 Final Output

At the end of the ordering process the system displays the amount to be paid followed by a thank-you message.

## 5. Functional Modules

The current functionality can be divided into three logical modules:

1. Menu Display and Menu Data

Stores item names and prices.

Displays the menu.

2. Order Input and Validation

Accepts customer choices.

Checks item availability.

Adds items to the order.

3. Bill Calculation and Output

Calculates the price.

Displays the final payable amount.

Displays completion messages.

## 6. Non-Functional Requirements

The project should satisfy the following -functional requirements:

### 6.1 Usability

The system should provide prompts and understandable messages so that a user can complete an order through the console.

### 6.2 Performance

The program should respond quickly for the predefined menu. Menu membership checking and price retrieval should be fast during execution.

### 6.3 Reliability

Only items that exist in the predefined menu should contribute to the order total.

### 6.4 Maintainability

Menu prices should be easy to modify without changing the ordering logic. Storing menu information in a dictionary supports this requirement.

The current implementation still requires refactoring because similar code is present in uploaded files.

### 6.5 Error Handling

The program should identify an item that's not present, in the menu and display an appropriate message rather than adding it to the bill.

## 7. Inputs

The system accepts:

- item name.

- Choice to add another item (Yes/No).

- Second item name when the user chooses Yes.

## 8. Outputs

The system produces:

- message.

- Menu and prices.

- Confirmation when an item is successfully added.

- Message when an item is unavailable.

- Total amount to pay.

- Thank-you message.

## 9. Basic Workflow

Start

↓

Display Cafe Welcome Message

↓

Display Menu

↓

Initialize Order Total

↓

Enter First Item

↓

Check Item Availability

├── Available → Add Price

└── Not Available → Display Error Message

↓

Ask Whether Another Item Is Required

├── Yes →. Validate Second Item

└── No → Continue

↓

Display Total Amount

↓

Display Thank You Message

↓

End

## 10. Technology Used

- Python 3

- Python dictionary

- Variables

- statements

- User input/output

- Arithmetic operations

- f-strings

- Command-line interface

No external libraries or database are required by the current implementation.

## 11. Current Limitations

The current project is a first version. Its main limitations are:

- two item selections are supported in the current workflow.

- Item quantities are not supported.

- There is no database.

- Orders are not saved after the program ends.

- There is no login or user management.

- There is no payment facility.

- There is no GUI.

- There is no inventory tracking.

- Automated testing has not yet been implemented.

- The uploaded Python files contain duplicated code and should be reorganized into genuinely separate modules before final submission.

## 12. Possible Future Enhancements

The system can be extended by:

- Allowing menu-item selections.

- Adding item quantities.

- Creating a cart/order list.

- Adding taxes and discounts.

- Generating a receipt.

- Adding database storage.

- Adding order history.

- Adding inventory management.

- Creating an interface.

- Adding automated unit tests.

- Improving input validation and case handling.

- Separating the code into modules/classes.

## 13. Project Goal

The overall goal is to demonstrate how a real-world cafe ordering problem can be translated into a software solution using Python programming concepts.

The project is intended to provide a foundation that can later be expanded into a complete cafe management system.

