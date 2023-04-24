import React, {useState} from 'react';
import { styled,  useMediaQuery, Button, TextField, Typography, FormGroup, FormControlLabel, Checkbox, Divider } from '@mui/material';
import { Box } from '@mui/system';

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
        .then(response => response.json())
        .then(data => {
            console.log('Success:', data);
            if (rememberMe) {
                sessionStorage.setItem('rememberMe', data.username);
            }
            sessionStorage.setItem('user', data);
            window.location.href = '/profile';
        }
        )
    }

    return(
        
        <LogInBox
        sx={{position: 'absolute',
          top: '50%',
          left: '50%',
          transform: 'translate(-50%, -50%)',
          width:  isSmallScreen ? "80vw" : "30vw",
          height:  isSmallScreen ? "60vh" : "calc(100vh - 540px)",
          minHeight: 350,
        //   bgcolor: 'background.paper',
          border: '2px solid #000',
          boxShadow: 24,
          p:4,
        //   backgroundColor: '#fcfcf9'
        //   backgroundColor: '#ffffff'    
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
        </LogInBox>
        
    )
}

export default LoginPage;
/* Minor Details: 
1. Add shadow behind Login Box (like the background shadow)
2. Modify box to darker color (black?) when changed to dark mode
*/