import { Grid } from '@mui/material';
import React from 'react';
import EventsCalendar from '../components/EventsCalendar';

function EventsPage() {
  return (
    <Grid container spacing={2} justifyContent="center">
        <Grid item xs={12}>
          <EventsCalendar></EventsCalendar>
        </Grid>
      </Grid>
    
    
  );
}

export default EventsPage;