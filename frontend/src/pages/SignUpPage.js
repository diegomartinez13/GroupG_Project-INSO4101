import React from 'react';
import { Button, TextField, Typography, Divider } from '@mui/material';
import { Box } from '@mui/system';


const SignUpPage = () => {


    return(
        <Box
        sx={{position: 'absolute',
          top: '50%',
          left: '50%',
          transform: 'translate(-50%, -50%)',
          width: 300,
          height: 400,
          bgcolor: 'background.paper',
          border: '2px solid #000',
          boxShadow: 24,
          p:4,
          alignContent: 'center'
          }} 
          >

            <Box 
            sx={{ my: 3, mx: 2 }}
            >
                <Typography variant='body1'>Email Address</Typography>
                    <TextField 
                    id="outlined-basic" 
                    variant="outlined"
                    size='small' />

                <Typography variant='body1'>Password</Typography>
                    <TextField 
                    id="outlined-basic" 
                    variant="outlined" 
                    size='small' />

                <Typography variant='body1'>Confirm Password</Typography>
                    <TextField 
                    id="outlined-basic" 
                    variant="outlined" 
                    size='small' />

                <p></p>

                <Button variant='contained'>Sign In</Button>
            </Box>
                
            <Divider variant="middle"/>

            <Box 
            sx={{ my: 3, mx: 2 }}    
            >
                Already registered? 
                <Button href='/login'>Log In</Button>
            </Box>          

        </Box>
    )
}

export default SignUpPage;
/* Minor Details: 
1. Add shadow behind Login Box (like the background shadow)
2. Modify box to darker color (black?) when changed to dark mode
*/