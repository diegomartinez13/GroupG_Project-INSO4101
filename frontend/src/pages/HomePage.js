import React from 'react';
import { Container, Grid } from '@mui/material';

function HomePage() {
  return (
    <div style={{ display: 'flex' }}>
      <main style={{ flexGrow: 1, padding: '16px' }}>
        <div style={{ height: '64px' }} />
        <Container maxWidth="lg">
          <Grid container spacing={3}>
            {/* Add content for the home page here */}
          </Grid>
        </Container>
      </main>
    </div>
  );
}

export default HomePage;