
## Stage 0
Command: `python checkpoint.py`
Result: PASS hello HTTP 200

## Stage 1
Command: `python checkpoint.py`
Result: PASS root and health JSON

## Stage 2
Command: `python checkpoint.py`
Result: PASS list, single, missing JSON 404

## Stage 3
Command: `python checkpoint.py`
Result: PASS create 201, list update, validation 400

## Stage 4
Command: `python checkpoint.py`
Result: PASS full CRUD: 200/201/204/400/404
