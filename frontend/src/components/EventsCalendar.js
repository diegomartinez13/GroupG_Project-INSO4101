import React, { Component } from "react";
import { Calendar, momentLocalizer } from "react-big-calendar";
import moment from "moment";
import "react-big-calendar/lib/css/react-big-calendar.css";
import styled from "@mui/material/styles/styled";

const localizer = momentLocalizer(moment);

// Add styled Calendar to get theme colors
const StyledCalendar = styled(Calendar)(({ theme }) => ({
  backgroundColor: theme.palette.surface.main,
  color: theme.palette.surface.text,
  '& .rbc-event': {
    backgroundColor: theme.palette.primary.main,
    color: theme.palette.primary.text,
  },
}));

class EventsCalendar extends Component {
  
  state = {
    events: [
      {
        start: moment().toDate(),
        end: moment()
          .add(1, "days")
          .toDate(),
        title: "Recycling Event"
      }
    ]
  };

  render() {
    return (
        <StyledCalendar
          localizer={localizer}
          defaultDate={new Date()}
          defaultView="month"
          events={this.state.events}
          style={{ height: "80vh" , alignContent: "center", alignItems: "center", justifyContent: "center"}}
          
        />
    );
  }
}

export default EventsCalendar;