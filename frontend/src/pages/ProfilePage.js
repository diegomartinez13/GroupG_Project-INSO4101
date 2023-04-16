import { Button } from '@mui/material';
import React, {useState} from 'react';


function ProfilePage() {

  return (
    <div>
      <h1>Profile</h1>
      <Button variant="outlined" onClick={() => {sessionStorage.clear(); window.location.href = '/login'}}
      >
        Sign Out
      </Button>

      {/* <Button variant="text" href="/login">
        Login
      </Button> */}

    </div>
  );
}

export default ProfilePage;