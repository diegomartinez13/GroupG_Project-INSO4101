import React, {useState} from 'react';
import { styled,  useMediaQuery, Button, TextField, Typography, Divider } from '@mui/material';
import { Box } from '@mui/system';

const SignUpUrl = 'http://localhost:5000/register';

const SignUpBox = styled(Box)(({ theme }) => ({
    color: theme.palette.surface.onVariant,
    alignContent: 'center',
    justifyContent: 'center',
  }));

  const SignUpTextField = styled(TextField)(({ theme }) => ({
    color: theme.palette.surface.onVariant,
    alignContent: 'center',
    justifyContent: 'center',
    '& input': {
        color: theme.palette.surface.onVariant,
      },
    }));

const SignUpPage = () => {

    const isSmallScreen = useMediaQuery('(max-width: 600px)');
    const [inputValues, setInputValues] = useState({
        username: '',
        password: '',
        password_confirmation: '',
    });

    const handleSignUp = () => {
      console.log('Sign Up');
        fetch(SignUpUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(inputValues)
        })
        .then(response => { 
          response.json();
          if (response.status === 201) {
            window.location.href = '/login';
          }
        })
        .then(data => {
            console.log('Success:', data);
        }
        )
    }


    return(
        <SignUpBox
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

            <SignUpBox 
            sx={{ my: 3, mx: 2 }}
            >
                <Typography variant='body1'>Username</Typography>
                    <SignUpTextField 
                    required
                    fullWidth
                    id="outlined-basic" 
                    variant="outlined"
                    size='small'
                    value={inputValues.username}
                    onChange={(e) => setInputValues({...inputValues, username: e.target.value})}
                    error={inputValues.username.length > 50}
                     />

                <Typography variant='body1'>Password</Typography>
                    <SignUpTextField 
                    required
                    fullWidth
                    id="outlined-basic" 
                    variant="outlined" 
                    type='password'
                    size='small'
                    value={inputValues.password}
                    onChange={(e) => setInputValues({...inputValues, password: e.target.value})}
                    />

                <Typography variant='body1'>Confirm Password</Typography>
                    <SignUpTextField 
                    required
                    fullWidth
                    id="outlined-basic" 
                    variant="outlined" 
                    type='password'
                    size='small' 
                    value={inputValues.password_confirmation}
                    onChange={(e) => setInputValues({...inputValues, password_confirmation: e.target.value})}
                    error={inputValues.password !== inputValues.password_confirmation}
                    />

                <p></p>

                <Button variant='contained' 
                onClick={() => handleSignUp()}
                disabled={inputValues.password !== inputValues.password_confirmation || inputValues.username === '' || inputValues.password === '' || inputValues.password_confirmation === ''}
                >Register</Button>
            </SignUpBox>
                
            <Divider variant="middle"/>

            <SignUpBox 
            sx={{ my: 3, mx: 2 }}    
            >
                Already registered? 
                <Button href='/login'>Log In</Button>
            </SignUpBox>          

        </SignUpBox>
    )
}

export default SignUpPage;
/* Minor Details: 
1. Add shadow behind Login Box (like the background shadow)
2. Modify box to darker color (black?) when changed to dark mode
*/