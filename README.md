# Pong Eternal

Paco PASTOR
Pierrick IDE
Kevin GREVIN
Raphael RAULT

Pong game with tests

## Quickstart :

_Make sure you have Python 3.11.6 installed_

```bash
python3 -m venv venv # Create an empty python virtual environment
source venv/bin/activate # Enable it
pip3 install -r requirements.txt # Install dependencies
python3 main.py # Launch game
```

## Launch tests :

```bash
python3 -m unittest
```

## Test cases :

### Ball tests

| Test Case | Expected Result           |
| --------- | ------------------------- |
|test_update_image|Updated image is not the same as old image|
|test_start       |Ball direction is same as ball orientation|
|test_move        |Check correct ball movement|
|test_radian      |Basic test for radian calculation|
|test_rotate      |Correct ball rotation that changes orientation variable|

### Menu tests

| Test Case | Expected Result           |
| --------- | ------------------------- |
|test_start_menu          |Verify correct instanciation of menu items |
|test_menu_too_small      |Ensure that a too small menu will raise an exception|
|test_menu_negative_values|Ensure that negative menu dimensions will raise an exception|

### Paddle tests

| Test Case | Expected Result           |
| --------- | ------------------------- |
|test_move_up         |Test move up by 3 pixels|
|test_move_up_border  |Verify that up border is correctly blocking paddle|
|test_move_down       |Test move down by 3 pixels|
|test_move_down_border|Verify that down border is correctly blocking paddle|