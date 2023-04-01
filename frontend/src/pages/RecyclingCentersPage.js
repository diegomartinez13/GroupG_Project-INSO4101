import React from 'react';
import {  Container } from '@mui/material';
import RecyclingCentersMap from "../components/RecyclingCentersMap";


function RecyclingCentersPage() {
  return (
    <Container maxWidth="lg">
      <RecyclingCentersMap />
    </Container>
  );
}

export default RecyclingCentersPage;