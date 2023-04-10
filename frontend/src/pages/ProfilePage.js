import { Card, Button, Modal } from '@mui/material';
import { Box } from '@mui/system';
import React from 'react';
import { styled } from '@mui/material';
import LoginPage from '../pages/LoginPage';

// function ProfilePage() {
const ProfilePage = () => {
  // css style info
  const boxStyle = styled(Card)(({ theme }) => ({
    width: 300,
    height: 300,
    backgroundColor: theme.palette.surface.variant,
    alignContent: 'center',
    justifyContent: 'center',
    padding: '0.5em',
    margin: '0.5em',
    maxWidth: '50rem'
  }
  ));

  const [open, setOpen] = React.useState(false);
  const handleOpen = () => setOpen(true);
  const handleClose = () => setOpen(false);

  return (
    <div>
      <h1>Profile</h1>
      {/* if userLoggedIn == True */}
          {/* Profile page */}
      {/* if userLoggedIn == False */}

      {/* <Button variant="outlined"  onClick={handleOpen}>
        Sign Up      
      </Button>

      <Modal open={open} onClose={handleClose}>
          <Box sx={{position: 'absolute',
          top: '50%',
          left: '50%',
          transform: 'translate(-50%, -50%)',
          width: 400,
          height: 250,
          bgcolor: 'background.paper',
          border: '2px solid #000',
          boxShadow: 24,
          p:4
          }}         
          >
            
          
            </Box>
      </Modal> */}

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

/* 
1. Instead of boxes, do two buttons: sign up button and login button
  -> each button goes to its respective Page
  -Sign in: 
  forum: email
  forum: password
  button: sign in
  line: ---or---
  button: new to the page? sign up here!
          ""? create your account here

2. How to make it so button changes to login/sign in page?
*/