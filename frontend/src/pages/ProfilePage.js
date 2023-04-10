import { Button } from '@mui/material';
import React from 'react';


function ProfilePage() {

  return (
    <div>
      <h1>Profile</h1>
      {/* if userLoggedIn == True */}
          {/* Profile page */}

      {/* if userLoggedIn == False */}
      <Button variant="outlined" href="/signup">
        Sign Up
      </Button>

      <Button variant="text" href="/login">
        Login
      </Button>

    </div>
  );
}

export default ProfilePage;