# Textual Live Editing Issue
A minimal reproducible example of CSS live editing issue in Textual.

## Usage
Clone the repo.
```shell
git clone git@github.com:Klavionik/textual-live-editing-issue.git
```

Create and activate a new venv.

```shell
cd textual-live-editing-issue
python -m venv venv
source venv/bin/activate
```

Install dependencies.

```shell
pip install -r requirements.txt
```

Run the app in dev mode.

```shell
textual run --dev main:TheApp
```

## How to reproduce
Change the Label color inside `app.tcss` and you'll see it changing in the terminal. 
Press `F` to activate the screen and do the same inside `screen.tcss`. You'll see that 
no hot reload happens.
