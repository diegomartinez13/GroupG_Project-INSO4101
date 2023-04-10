import React from 'react';
import { Button, TextField, Typography, FormGroup, FormControlLabel, Checkbox, Divider } from '@mui/material';
import { Box } from '@mui/system';


const LoginPage = () => {


    return(
        <Box
        sx={{position: 'absolute',
          top: '50%',
          left: '50%',
          transform: 'translate(-50%, -50%)',
          width: 300,
          height: 350,
          bgcolor: 'background.paper',
          border: '2px solid #000',
          boxShadow: 24,
          p:4
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

                <FormGroup>
                    <FormControlLabel control={<Checkbox defaultChecked />} label="Remember me" />
                </FormGroup>

                <Button variant='contained'>Sign In</Button>
            </Box>
                
            <Divider variant="middle"/>

            <Box
            sx={{ my: 3, mx: 2 }}    
            >
                New around here? 
                <Button href="/signup">Sign Up</Button>
            </Box>          

        </Box>
    )
}

export default LoginPage;
/* Minor Details: 
1. Add shadow behind Login Box (like the background shadow)
2. Modify box to darker color (black?) when changed to dark mode
*/