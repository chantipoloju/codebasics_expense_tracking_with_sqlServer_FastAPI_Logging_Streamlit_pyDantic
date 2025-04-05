

# Expense Management System


This project is an expense management system that consists of a Streamlit frontend application, SQL for database and a FastAPI backend server.

This application allows users to manage their daily expenses, view analytics, and interact with a database for storing and retrieving expense data.

## Features

- Add or update daily expenses with details like amount, category, and notes.
- Analyze expenses over a date range with visualizations.
- Store expense data in a MySQL database.
- Backend powered by FastAPI for handling requests.
- Frontend built with Streamlit for a user-friendly experience.
- Secure authentication and user management.
- Export expenses as CSV or Excel for record-keeping.

## Tech Stack

- **Backend**: FastAPI, Uvicorn
- **Frontend**: Streamlit
- **Database**: MySQL
- **Other Libraries**: Pydantic, Requests

## Project Structure

- **frontend/**: Contains the Streamlit application code.
- **backend/**: Contains the FastAPI and SQL backend server code.
- **tests/**: Contains the test cases for both frontend and backend.
- **requirements.txt**: Lists the required Python packages.
- **README.md**: Provides an overview and instructions for the project.

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/mehulcode12/codebasics_expense_tracking_with_sqlServer_FastAPI_Logging_Streamlit_pyDantic.git
   cd expense-management-system
   ```
2. **Install dependencies:**   
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the SQL server:**   
   ```bash
   Use SQL WorkBench and import the sql file from root directory. make sure you provide proper host and password(as per your system)
   ```
4. **Run the FastAPI server:**   
   ```bash
   uvicorn backend.server:app --reload
   ```
5. **Run the Streamlit app:** 
    (note: use second terminal/cmd to execute this)
   ```bash
   streamlit run frontend/app.py
   ```

## API Endpoints

- **GET /expenses/{expense_date}**: Fetch expenses for a specific date.
- **PUT /expenses/{expense_date}**: Update expenses for a specific date.
- **POST /analytics/**: Fetch expense summary for a date range.
- **POST /export/**: Export expense data as CSV or Excel.

## Project Structure

```
Expense_Tracking/
├── backend/                           # Backend folder containing FastAPI server code
│   ├── server.py                      # FastAPI server entry point
│   ├── server.log                     # log file
│   ├── db_helper.py                   # Database helper functions for CRUD operations
│   ├── logging_setup.py               # Logging configuration for the backend
│   └── tests/                         # Backend test cases
│       ├── test_server.py             # Tests for the FastAPI server
│       └── test_db_helper.py          # Tests for database helper functions
│
├── frontend/                          # Frontend folder containing Streamlit app code
│   ├── app.py                         # Streamlit app entry point
│   ├── add_update_tab.py              # Code for the "Add/Update Expense" tab
│   ├── analytics_category.py          # Code for the "View Analytics by Category" tab
│   ├── analytics_month.py             # Code for the "View Analytics by Month" tab
│   ├── debugging.py                   # Code made for debugging and integratoin purpose
│
├── database/                          # Folder for database-related scripts and configurations
│   ├── init_db.sql                    # SQL script to initialize the database and create tables
│   ├── db_config.py                   # Database connection configuration
│   └── migrations/                    # Folder for database migration scripts
│       ├── 001_create_expenses_table.sql
│       └── 002_add_indexes.sql
│
├── tests/                             # Root-level folder for integration tests
│   ├── __init__.py                    # Marks the folder as a Python package
│   └── backend/                       # Folder for database migration scripts
│       ├── test_db_helper.sql         # Tests database helper functions for fetching and summarizing expense data.
│
│
├── requirements.txt                   # Python dependencies for the project
├── README.md                          # Project documentation
```

## Screenshots & Recordings

To better understand how the application works, here are some screenshots and recordings:

- **Screenshots**: 
1. ![Adding/Updating DATA](https://github.com/mehulcode12/codebasics_expense_tracking_with_sqlServer_FastAPI_Logging_Streamlit_pyDantic/blob/main/Screenshots/Screenshot%202025-04-04%20211357.png)
2. ![SQL database](https://github.com/mehulcode12/codebasics_expense_tracking_with_sqlServer_FastAPI_Logging_Streamlit_pyDantic/blob/main/Screenshots/Screenshot%202025-04-04%20211418.png)
3. ![Server log file](https://github.com/mehulcode12/codebasics_expense_tracking_with_sqlServer_FastAPI_Logging_Streamlit_pyDantic/blob/main/Screenshots/Screenshot%202025-04-04%20211452.png)
4. ![Analytics 1](https://github.com/mehulcode12/codebasics_expense_tracking_with_sqlServer_FastAPI_Logging_Streamlit_pyDantic/blob/main/Screenshots/Screenshot%202025-04-04%20211331.png)
5. ![Analytics 2](https://github.com/mehulcode12/codebasics_expense_tracking_with_sqlServer_FastAPI_Logging_Streamlit_pyDantic/blob/main/Screenshots/Screenshot%202025-04-04%20211318.png)
6. ![Analytics 3](https://github.com/mehulcode12/codebasics_expense_tracking_with_sqlServer_FastAPI_Logging_Streamlit_pyDantic/blob/main/Screenshots/Screenshot%202025-04-04%20211306.png)

   
- **Screen Recording**:
- [CLick here](https://github.com/mehulcode12/codebasics_expense_tracking_with_sqlServer_FastAPI_Logging_Streamlit_pyDantic/blob/main/ScreenRecording.mp4)

Upload your screenshots and recordings to a publicly accessible location and update this section with the links.

## License

This project is licensed under the MIT License - see file for details.

## Contributing

Contributions are welcome! 

Need of Contributor:
1. Secure authentication and user management.
2. Export expenses as CSV or Excel for record-keeping.

Please follow these steps:
1. Fork the repository.
2. Create a new branch (`feature-branch`).
3. Commit your changes with clear messages.
4. Push the branch and create a Pull Request.

For major changes, open an issue first to discuss proposed modifications.

## Contact

For any questions or support, reach out to:

- **Email**: mehulligade12@gmail.com
- **GitHub Issues**: [Issue Tracker](https://github.com/mehulcode12/codebasics_expense_tracking_with_sqlServer_Logging_Streamlit_pyDantic_Streamlit/issues)

## Disclaimer

This project was inspired by the **Codebasics DSAI Bootcamp**. It is not entirely my original work but has been extended and customized for additional functionality.

