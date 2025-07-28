# Free Coding Project Planner

A command-line event planning application built in Python that allows users to create personal planners, schedule events, and manage their time effectively.

## Features

- **Multi-User Support**: Create separate planners for different people
- **Event Scheduling**: Add events with specific dates, start/end times, and priority levels
- **Conflict Detection**: Automatically detects scheduling conflicts and offers resolution options
- **Event Management**: View, add, and remove events from your schedule
- **Persistent Storage**: Events are saved to text files organized by date
- **Priority System**: Assign priority levels (1-10) to events for better organization

## How It Works

The application uses a time-based scheduling system where each day is divided into 1440 minutes (24 hours). Events are stored as time ranges, and the system tracks available time slots to prevent double-booking.

### Key Components

- **Event Class**: Represents individual events with name, date, start/end times, and priority
- **Planner Class**: Manages a user's schedule, handles event conflicts, and maintains available time slots
- **File Storage**: Each planner gets its own directory with date-based text files for event storage

## Installation

1. Clone or download the project files
2. Ensure you have Python 3.x installed
3. No additional dependencies required - uses only Python standard library

## Usage

### Starting the Application

```bash
python planner.py
```

### Main Menu Options

1. **Create a new planner** - Set up a planner for a new user
2. **Access existing planner** - Work with an existing user's schedule
3. **Exit** - Close the application

### Creating Events

When adding an event, you'll be prompted for:
- **Event name**: Description of the event
- **Date**: Format YYYY-MM-DD (e.g., 2024-12-25)
- **Start time**: Time in HH:MM format (e.g., 9:30)
- **AM/PM**: Specify morning or afternoon
- **End time**: Time in HH:MM format
- **Priority**: Scale of 1-10 (10 being highest priority)

### Planner Options

Once you're in a planner, you can:
1. **Add an event** - Schedule a new event
2. **See existing events** - View events for a specific date
3. **Remove an existing event** - Delete events from your schedule
4. **Return to home options** - Go back to main menu

### Conflict Resolution

If you try to schedule an event during a time that's already booked:
- The system will show you the conflicting event and its priority
- You can choose to replace the existing event with your new one
- The system will automatically update your available time slots

## File Structure

```
Free Coding Project Planner/
├── planner.py          # Main application file
├── README.md          # This file
└── [planner_name]/    # Directory created for each planner
    ├── YYYY-MM-DD.txt # Event files organized by date
    └── ...
```

## Example Usage

```
Type 1 to make a new planner, 2 to access an existing planner or 3 to exit: 
1
Who are you making a planner for?
Charlie
Planner for Charlie successfully created.
Would you like to add an event?
yes
Event: Study Session
Enter the date in the following format: YYYY-MM-DD: 2024-12-20
What time does it start? 14:30
am or pm?
pm
when does it end? 
16:00
am or pm?
pm
How much of a priority is it for you on a scale of 1-10? 8
2024-12-20
event successfully added
```

## Technical Details

- **Time Conversion**: The system converts HH:MM AM/PM format to minute-based calculations for precise scheduling
- **Conflict Detection**: Uses minute-by-minute time slot tracking to identify overlapping events
- **Data Persistence**: Events are stored in plain text files for easy backup and portability
- **Input Validation**: Includes basic validation for time formats and date inputs

## Future Enhancements

Potential improvements could include:
- Calendar view functionality
- Recurring events
- Event categories/tags
- Export to calendar applications
- Web interface
- Mobile app integration

## Contributing

This is a learning project for CS111. Feel free to experiment with the code and add new features!

## License

This project is open source and available for educational use.
