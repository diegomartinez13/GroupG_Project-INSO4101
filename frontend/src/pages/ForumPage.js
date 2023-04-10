import React from 'react';
import Forums from '../components/Forums';
import { Grid } from '@mui/material';


function ForumPage() {
  return (
    <Grid container spacing={2} justifyContent="center">
      <Forums></Forums>
    </Grid>
  );
}

export default ForumPage;