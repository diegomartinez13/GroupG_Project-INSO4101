import React, {useState} from 'react';
import { styled, Snackbar, useMediaQuery, Button, TextField, Typography, FormGroup, FormControlLabel, Checkbox, Divider, Alert } from '@mui/material';
import { Box } from '@mui/system';
import MuiAlert, { AlertProps } from '@mui/material/Alert';

const LogInUrl = 'http://localhost:5000/login';

const LogInBox = styled(Box)(({ theme }) => ({
    color: theme.palette.surface.onVariant,
    alignContent: 'center',
    justifyContent: 'center',
    style: {
        zIndex: 20,
    }
  }));

const LoginTextField = styled(TextField)(({ theme }) => ({
    color: theme.palette.surface.onVariant,
    alignContent: 'center',
    justifyContent: 'center',
    style: {
        zIndex: 20,
    },
    '& input': {
        color: theme.palette.surface.onVariant,
      },
    }));

const LoginPage = () => {

    const [inputValues, setInputValues] = useState({
        username: sessionStorage.getItem('rememberMe') || '',
        password: '',
    });

    const [popUp, setPopUp] = useState({
        open: false,
        vertical: 'top',
        horizontal: 'center',
        message: '',
    });

    const [alert, setAlert] = useState({
        open: false,
        severity: 'success',
        message: '',
     });

    const { vertical, horizontal, open } = popUp;

    const [rememberMe, setRememberMe] = useState(sessionStorage.getItem('rememberMe') != null && sessionStorage.getItem('rememberMe') != '' && sessionStorage.getItem('rememberMe') != undefined && sessionStorage.getItem('rememberMe') != 'undefined' ? true : false);


    const isSmallScreen = useMediaQuery('(max-width: 600px)');

    const handleLogIn = () => {
        console.log('Log In');
        fetch(LogInUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(inputValues)
        })
        .then(response => {

            if (response.status === 200) {
                setAlert({ open: true, severity: 'success', message: 'Success! You are now logged in.' });
                return response.json();
            } else {
                throw new Error("Invalid credentials");
            }
        })
        .then(data => {
            console.log('Success:', data);
            if (rememberMe) {
                sessionStorage.setItem('rememberMe', data.username);
            }
            console.log(data)
            sessionStorage.setItem('user', JSON.stringify(data));
            window.location.href = '/profile';
        }
        ).catch((error) => {
            console.error('Error:', error);
            setAlert({ open: true, severity: 'error', message: error + '. Please try again.' });        });
    }

    const handleClose = () => {
        setPopUp({ ...popUp, open: false, message: '' });
      };

      const handleAlertClose = (event, reason) => {
        if (reason === 'clickaway') {
           return;
        }
     
        setAlert({ ...alert, open: false });
     };

    return(
        
        <LogInBox
        sx={{position: 'absolute',
          top: '50%',
          left: '50%',
          transform: 'translate(-50%, -50%)',
          width:  isSmallScreen ? "80vw" : "30vw",
          height:  isSmallScreen ? "60vh" : "calc(100vh - 540px)",
          minHeight: 350,
          border: '1px solid',
          boxShadow: 10,
          p:4   
          }} 
          >
            {/* <Slide direction="down" in={true} mountOnEnter unmountOnExit > */}

            <LogInBox
            sx={{ my: 3, mx: 2 }}
            style = {{
                zIndex: 20,
              }}
            >
                <Typography variant='body1'>Username</Typography>
                    <LoginTextField 
                    fullWidth
                    required
                    id="outlined-basic" 
                    variant="outlined"
                    size='small'
                    placeholder='example@pr.com'
                    value={inputValues.username}
                    onChange={(e) => setInputValues({...inputValues, username: e.target.value})}
                
                      />

                <Typography variant='body1'>Password</Typography>
                    <LoginTextField 
                    fullWidth
                    required
                    id="outlined-basic" 
                    variant="outlined" 
                    size='small'
                    type='password'
                    placeholder='password'
                    value={inputValues.password}
                    onChange={(e) => setInputValues({...inputValues, password: e.target.value})}
                     />

                <FormGroup>
                    <FormControlLabel control={<Checkbox checked={rememberMe} onChange={(e) => setRememberMe(e.target.checked)} name="rememberMe"
                     />} label="Remember me" />
                </FormGroup>

                <Button variant='contained' disabled={inputValues.username === '' || inputValues.password === ''}
                onClick={() => handleLogIn()}>Log In</Button>
            </LogInBox>
                
            <Divider variant="middle"/>

            <LogInBox
            sx={{ my: 3, mx: 2 }}    
            >
                New around here? 
                <Button href="/signup"
                >Sign Up</Button>
            </LogInBox>          
            {/* </Slide> */}
            <Snackbar open={alert.open} autoHideDuration={6000} onClose={handleAlertClose}>
   <MuiAlert elevation={6} variant="filled" onClose={handleAlertClose} severity={alert.severity}>
      {alert.message}
   </MuiAlert>
</Snackbar>

            
        </LogInBox>
        
    )
}

export default LoginPage;