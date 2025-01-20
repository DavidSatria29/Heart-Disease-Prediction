## Overview
Heart Predict is a web-based application that leverages the power of the **Decision Tree Algorithm** to analyze user health data and predict the likelihood of heart failure. The Decision Tree algorithm was chosen for its ability to handle complex datasets and provide clear, interpretable results for users.


## Made With Django Framework

More information can be seen by pressing this link (https://www.djangoproject.com/)

## Install Dependencies

- install django framework
```bash
py -m pip install Django
```

- install library 
```bash
py -m pip install -r requirements.txt
```
## Further installations on graphviz

Grphviz has additional requirements to be used. Graphviz can only be used if installed directly through the web so that it can render the generated dot source code. You can install graphviz directly on the following web link (https://www.graphviz.org/download/). For Windows users can see the tutorial on the following link (https://forum.graphviz.org/t/new-simplified-installation-procedure-on-windows/224)

## Running migration and web

In the same directory as the 'manage.py' directory. run the command on the terminal 

```bash
py manage.py migrate
```

```bash
py manage.py runserver
```
