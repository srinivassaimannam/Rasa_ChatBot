## start
* greet
- utter_greet
> check_greet


## book

> check_greet
* cab_book
- utter_passengers
> check_start

## book_nano

> check_start
* nano
- form_info
- form{"name": "form_info"}
- form{"name": null}

## book_micro

> check_start
* micro
- form_info
- form{"name": "form_info"}
- form{"name": null}


## book_macro

> check_start
* macro
- form_info
- form{"name": "form_info"}
- form{"name": null}


## cancel

> check_greet
* cancel
- form_cancel
- form{"name": "form_cancel"}
- form{"name": null}


## details

> check_greet
* details
- form_details
- form{"name": "form_details"}
- form{"name": null}