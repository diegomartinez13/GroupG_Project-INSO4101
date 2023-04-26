import { Button, Avatar, Box, Card, CardContent, Typography, Grid, 
  LinearProgress, CardMedia, CardHeader, TextField, Input, InputLabel, Stack,
  FormLabel, FormControl, OutlinedInput, Slider } from '@mui/material';
import React from 'react';
import ModeEditIcon from '@mui/icons-material/ModeEdit';


function ProfilePage() {

  function LinearProgressWithLabel(props) {
    return (
      <Box sx={{ display: 'flex', alignItems: 'center' }}>
        {/* Linear Progress */}
        <Box sx={{ width: '100%', mr: 1 }}>
          <LinearProgress variant="determinate" {...props} />
        </Box>
        {/* Percent Label */}
        <Box sx={{ minWidth: 35 }}>
          <Typography variant="body2" color="text.secondary">{`${Math.round(
            props.value,
          )}%`}</Typography>
        </Box>
      </Box>
    );
  }

// Linear Progress Bar
  const [progress, setProgress] = React.useState(10);

  React.useEffect(() => {
    const timer = setInterval(() => {
      setProgress((prevProgress) => (prevProgress >= 100 ? 10 : prevProgress + 10));
    }, 800);
    return () => {
      clearInterval(timer);
    };
  }, []);





  return (

    <>
    <Button href="/profile-edit"
      sx={{
        position: 'absolute',
        right:45,
        transform: 'translate(-10px,-30px)'
      }} 
      > <ModeEditIcon fontSize='small'/> Record Activity  </Button>


    <Grid container 
      justifyContent="center"
    >

    <Card 
    sx={{
      maxWidth: '50rem',
      objectFit: 'cover',
      backgroundColor: '#fcfdf6',
      border: "none",
      boxShadow: "none" 
        // transform: 'translate(-50px,200px)'
        
        }}>
        
        <CardMedia/>
        <CardHeader  sx={{textAlign:'left'}}/>

          <Avatar 
                variant= "circular"
                sx={{
                  width:80,
                  height:80,
                  margin: 'auto'
                }} 
                src="/broken-image.jpg" 

                />

        <CardContent >            
          <FormControl disabled variant='standard' sx={{backgroundColor: 'white'}}>
            <OutlinedInput id='component-outlined'defaultValue='Michael Fischback'></OutlinedInput>
          </FormControl>
        </CardContent>


        <CardContent >            
          <FormControl disabled variant='standard' sx={{backgroundColor: 'white', }}>
            <OutlinedInput id='component-outlined'defaultValue='Rewards Points Earned'></OutlinedInput>
          </FormControl>
        </CardContent>


        <CardContent >            
          <FormControl disabled variant='standard' sx={{backgroundColor: 'white'}}>
            <OutlinedInput id='component-outlined'defaultValue='Amount Recycled'></OutlinedInput>
          </FormControl>
        </CardContent>


        <CardContent >            
          <FormControl disabled variant='standard' sx={{backgroundColor: 'white'}}>
            <OutlinedInput id='component-outlined'defaultValue='Contribution Hours'></OutlinedInput>
          </FormControl>
        </CardContent>

      </Card>


      {/* Goals */}
      <Card 
        sx={{width:400,
          padding: '0.5em',
          margin: '0.5em',
          maxWidth: '50rem',
          objectFit: 'cover',
          border: "none"
          }}>
     
        <CardContent>          
        <Typography variant='h5'>Goals</Typography>
          Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quos blanditiis tenetur unde suscipit, quam beatae rerum inventore consectetur, neque doloribus, cupiditate numquam dignissimos laborum fugiat deleniti? Eum quasi quidem quibusdam.
        </CardContent>

        <CardContent>

          <Typography variant="body1" color="textSecondary" component="p">
            Goals 1
          </Typography>
          <LinearProgress variant='determinate' value={60}
            sx={{height: 20, maxWidth:350}} 
            />

          <Typography variant="body1" color="textSecondary" component="p">
            Goal 2
          </Typography>
          <LinearProgress variant='determinate' value={60}            
          sx={{height: 20 , maxWidth:350}} 
            />

          <Typography variant="body1" color="textSecondary" component="p">
            Goal 3
          </Typography>
          <LinearProgress variant='determinate' value={60}            
          sx={{height: 20 , maxWidth:350}} 
            />

          <Typography variant="body1" color="textSecondary" component="p">
            Goal 4
          </Typography>
          <LinearProgress variant='determinate' value={progress}            
            sx={{height: 20 , maxWidth:350}} 
            />


          <Typography variant="body1" color="textSecondary" component="p">
            Goal 5
          </Typography>
          <LinearProgressWithLabel value={progress} sx={{height: 20 , maxWidth:350}}/>

        </CardContent>


      </Card>

      {/* Efforts */}
      <Card sx={{width: 650,     
      padding: '0.5em',
      margin: '0.5em',
      maxWidth: '50rem',
      objectFit: 'cover'
      }}>
        <CardMedia
          height="200"
        />

        <CardContent>

          <Typography variant='h5'>Recorded Recycling Efforts</Typography>

          <Typography variant="body1" color="textSecondary" component="p">
            Donated clothing
          </Typography>
          <LinearProgress variant='determinate' value={60}
          // sx={{height: 10}}
          />

          <Typography variant="body1" color="textSecondary" component="p">
            Started composting at home
          </Typography>
          <LinearProgress variant='determinate' value={60}/>

          <Typography variant="body1" color="textSecondary" component="p">
            Recycled for a week
          </Typography>
          <LinearProgress variant='determinate' value={60}/>

          <Typography variant="body1" color="textSecondary" component="p">
            Recycled for 6 months
          </Typography>
          <LinearProgress variant='determinate' value={60}/>

          <Typography variant="body1" color="textSecondary" component="p">
            Donated clothing
          </Typography>
          <LinearProgress variant='determinate' value={60}/>


        </CardContent>

      </Card>

      </Grid>
  
</>

  )
}

export default ProfilePage;
/*
Minor Details:
1.there's a white area (box) behind Recorder Recycling Efforts, 
  no idea what's that about.
2. Modify box to darker color (black?) when changed to dark mode done
*/