# Pong Eternal

Paco PASTOR
Pierrick IDE
Kevin GREVIN
Raphael RAULT

Pong game with tests

## Quickstart :

_Make sure you have Python 3.11.6 installed_

```bash
pip3 install -r requirements.txt # Install dependencies
python3 main.py # Launch game
```
## Gameplay :

| Mode | touche haut joueur 1 | touche bas joueur 1 | touche haut joueur 2 | touche bas joueur 2 |
|------|----------------------|---------------------|----------------------|---------------------|
|Joueur contre joueur | `z`| `s` | `arrow up` |  `arrow down` |
|Joueur contre robot  | `z`| `s` | ` |   |

## Launch tests :

```bash
python3 -m unittest
```

## Test cases :

setUp() method in each TestCase class is executed at the beginning of each test.

### Ball tests

| Test Case | Expected Result           |
| --------- | ------------------------- |
|test_update_image|Updated image is not the same as old image|
|test_start       |Ball direction is same as ball orientation|
|test_movement    |Check ball is moving|
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

### Event tests

| Test Case | Expected Result           |
| --------- | ------------------------- |
|test_wrong_event|When an event does not exists, raise a TypeError exception|

### Game tests

| Test Case | Expected Result           |
| --------- | ------------------------- |
|test_ball_out    |Verify handling_event method behavior on ball out event (return False)|
|test_ball_in     |Verify handling_event method behavior on any event (return True)|
