import React from 'react';
import Avatar from "react-avatar-edit";
// import EasyEdit from 'react-easy-edit';
import EditIcon from '@mui/icons-material/Edit';
import DeleteIcon from '@mui/icons-material/Delete';
import CloseIcon from '@mui/icons-material/Close';
import AddIcon from '@mui/icons-material/Add';

import { styled, Button,  Box, Card, CardContent, Typography, Grid, 
    LinearProgress, CardMedia, CardHeader, TextField, Slider, Modal, 
    IconButton } from '@mui/material';



const ProfileTextField = styled(TextField)(({ theme }) => ({
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

// Modal  
function DeleteModal(){
    const [open, setOpen] = React.useState(false);
    const handleOpen = () => setOpen(true);
    const handleClose = () => setOpen(false);
 
    return (
      <React.Fragment>    

        <IconButton aria-label="delete" onClick={handleOpen} >
                <DeleteIcon sx={{ color:'grey'}} />
        </IconButton>

        <Modal
          open={open}
          onClose={handleClose}
          aria-labelledby="delete-modal-title"
          aria-describedby="delete-modal-description"
        >
          <Box 
          
          sx={{position: 'absolute',
          top: '50%',
          left: '50%',
          transform: 'translate(-50%, -50%)',
          minHeight: 150,
          minWidth:300,
          border: '1px solid',
          boxShadow: 10,
          p:4,
          backgroundColor: 'white'
          }}
          >
            <IconButton onClick={handleClose} sx={{ color:'grey',
                position: 'absolute',
                right:45,
                transform: 'translate(20px,-10px)'
                }} > 
                <CloseIcon sx={{ color:'grey' }} /> 
            </IconButton>

            <Typography id="modal-modal-title" variant="h6" component="h2">
                    Delete this effort?
                </Typography>
                <Typography id="modal-modal-description" sx={{ mt: 2 }}>
                    If you decide to delete this effort, it will be gone
                </Typography>

            <Button onClick={handleClose} sx={{ color:'red', transform: 'translate(260px,10px)', appearance:'subtle'}} > Delete </Button>


          </Box>
        </Modal>
      </React.Fragment>
    );
  }


function EditModal(){
    const [open, setOpen] = React.useState(false);
    const handleOpen = () => setOpen(true);
    const handleClose = () => setOpen(false);
 
    return (
      <React.Fragment>    

        <Button aria-label="edit" onClick={handleOpen}>
                <EditIcon sx={{ color:'grey'}} />
        </Button>

        <Modal
          open={open}
          onClose={handleClose}
          aria-labelledby="edit-modal-title"
          aria-describedby="edit-modal-description"
        >
          <Box 
          
          sx={{position: 'absolute',
          top: '50%',
          left: '50%',
          transform: 'translate(-50%, -50%)',
          minHeight: 130,
          minWidth:300,
          border: '1px solid',
          boxShadow: 10,
          p:4,
          backgroundColor: 'white'
          }}
          >
            <IconButton onClick={handleClose} sx={{ color:'grey',
                position: 'absolute',
                right:45,
                transform: 'translate(20px,-10px)'
                }} > 
                <CloseIcon sx={{ color:'grey' }} /> 
            </IconButton>

            <Typography id="modal-modal-title" variant="h6" component="h2">
                    Edit Effort
                </Typography>


            <TextField
            id="edit-modal-description"
                    fullWidth             
                    // id="outlined-multiline-static"
                    variant="outlined"
                    size='small'
                    placeholder=' '
                    sx={{ transform: 'translate(0px,5px)'  }}

                ></TextField> 
                <Slider sx={{height:15, transform: 'translate(3px,20px)'}}/>


          </Box>
        </Modal>
      </React.Fragment>
    );
  }

function EditActivityPage(props) {

    // Edit Avatar/Image
    const[image, setImage] = React.useState('');
    function handleImage(e) {
        console.log(e.target.files)
        setImage(e.target.files[0])
    }

    // Preview Image
    const [preview, setPreview] = React.useState(null);
    function onClose() {
        setPreview(null);
    }
    function onCrop(pv) {
        setPreview(pv);
    }
    function onBeforeFileLoad(elem) {
        if (elem.target.files[0].size > 71680) {
        alert("File is too big!");
        elem.target.value = "";
        }
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

   

    return(
        <>    

        <header sx={{transform: 'translate(-10px,-30px)', variant:'h1'  }}> Edit Page</header>
    
    {/*Save Button (upper right)  */}
        <Button href="/profile"
            sx={{
            position: 'absolute',
            right:45,
            transform: 'translate(-10px,-30px)'
            }} 
            >  Save </Button>


        <Grid container
        justifyContent='center'>
            
    {/*Avatar  */}
        <Card 
            sx={{
            padding: '0.5em',
            margin: '0.5em',
            maxWidth: '50rem',
            objectFit: 'cover',
            width: 300,
            // backgroundColor: '#fcfdf6',
            // border: "none",
            // boxShadow: "none" 
                // transform: 'translate(-50px,200px)'
        }}>
        
            <CardMedia/>
            <CardHeader  sx={{textAlign:'left'}}/>

            <Avatar
                width={200}
                height={200}
                onCrop={onCrop}
                onClose={onClose}
                onBeforeFileLoad={onBeforeFileLoad}
                src={null}
            />
            {/* {preview && <img src={preview} alt="Preview" />} */}
            {/* <input type='file' name='file' onChange={handleImage}/> */}
            <input hidden accept="image/*" type="file" />

            <Button 
            // onClick={this.fileUploadHandler}  
            >Submit</Button>



            <Typography variant='body1'>Name</Typography>
                <ProfileTextField 
                fullWidth
                id="outlined-basic" 
                variant="outlined"
                size='small'
                placeholder='Michael Fischback'
                // value={inputValues.name}
                // onChange={(e) => setInputValues({...inputValues, name: e.target.value})}
                    />
                
            <Typography variant='body1'>Rewards Point Granted</Typography>
                <ProfileTextField 
                fullWidth
                disabled
                id="outlined-basic" 
                variant="outlined"
                size='small'
                placeholder=' '
                // value={inputValues.rewards}
                // onChange={(e) => setInputValues({...inputValues, rewards: e.target.value})}
                    />

            <Typography variant='body1'>Amount Recycled</Typography>
                <ProfileTextField 
                fullWidth
                disabled
                id="outlined-basic" 
                variant="outlined"
                size='small'
                placeholder=' '
                // value={inputValues.amountRecycled}
                // onChange={(e) => setInputValues({...inputValues, amountRecycled: e.target.value})}
                    />


            <Typography variant='body1'>Contribution Hours</Typography>
                <ProfileTextField 
                fullWidth
                disabled
                id="outlined-basic" 
                variant="outlined"
                size='small'
                placeholder=' '
                // value={inputValues.hoursContributed}
                // onChange={(e) => setInputValues({...inputValues, hoursContributed: e.target.value})}
                    />

        </Card>
      
    {/* Goals */}
      <Card
        sx={{
            // width:400,
            maxWidth:400,
            padding: '0.5em',
            margin: '0.5em',
            maxWidth: '50rem',
            objectFit: 'cover',
            // border: "none"
            // transform: 'translate(-50px,200px)'
    }}>

        <CardContent>
        <Typography variant='h5'>Goals</Typography>
            <ProfileTextField 
                fullWidth
                multiline
                rows={4}                
                id="outlined-multiline-static"
                variant="outlined"
                size='small'
                placeholder=' '
                // value={inputValues.goalsDescription}
                // onChange={(e) => setInputValues({...inputValues, goalsDescription: e.target.value})}
                    />
        </CardContent>
        <Typography variant='body1'>Goal 1</Typography>
            <ProfileTextField 
                fullWidth              
                id="outlined-basic"
                variant="outlined"
                size='small'
                placeholder='Goal 1'
                // value={inputValues.goal}
                // onChange={(e) => setInputValues({...inputValues, goal: e.target.value})}
                    />
                {/* enter value to set linear progress */}
                {/* by inputting value or by using a slider */}
            <Slider sx={{height:10, marginX:1, maxWidth:220}}/>

            <Typography variant='body1'>Goal 1</Typography>
            <ProfileTextField 
                fullWidth              
                id="outlined-basic"
                variant="outlined"
                size='small'
                placeholder='Goal 1'
                // value={inputValues.goal}
                // onChange={(e) => setInputValues({...inputValues, goal: e.target.value})}
                    />
                {/* enter value to set linear progress */}
                {/* by inputting value or by using a slider */}
            <Slider sx={{height:10, marginX:1, maxWidth:220}}/>


            <Typography variant='body1'>Goal 1</Typography>
            <ProfileTextField 
                fullWidth              
                id="outlined-basic"
                variant="outlined"
                size='small'
                placeholder='Goal 1'
                // value={inputValues.goal}
                // onChange={(e) => setInputValues({...inputValues, goal: e.target.value})}
                    />
                {/* enter value to set linear progress */}
                {/* by inputting value or by using a slider */}
            <Slider sx={{height:10, marginX:1, maxWidth:220}}/>



            <Typography variant='body1'>Goal 1</Typography>
            <ProfileTextField 
                fullWidth              
                id="outlined-basic"
                variant="outlined"
                size='small'
                placeholder='Goal 1'
                // value={inputValues.goal}
                // onChange={(e) => setInputValues({...inputValues, goal: e.target.value})}
                    />
                {/* enter value to set linear progress */}
                {/* by inputting value or by using a slider */}
            <Slider sx={{height:10, marginX:1, maxWidth:220}}/>


      </Card>




    {/* EFFORTS */}
      <Card
        sx={{
            width: 550,     
            padding: '0.5em',
            margin: '0.5em',
            maxWidth: '50rem',
            objectFit: 'cover'
        // width:  isSmallScreen ? "80vw" : "30vw",
        // height:  isSmallScreen ? "60vh" : "calc(100vh - 540px)"
            // transform: 'translate(-50px,200px)'
    }}>
        <CardMedia/>

            <CardContent>

            <Typography variant='h5'>Recorded Recycling Efforts</Typography>

            <Typography variant="body1" color="textSecondary" component="p">
                Donated clothing
            </Typography>
            <LinearProgress variant='determinate' value={60} sx={{height: 10}}/>
                
            <EditModal/>            
            <DeleteModal/>


            <Typography variant="body1" color="textSecondary" component="p">
                Started composting at home
            </Typography>
            <LinearProgress variant='determinate' value={60} sx={{height: 10}} />
            
            <EditModal/>
            <DeleteModal/>


            <Typography variant="body1" color="textSecondary" component="p">
                Recycled for a week
            </Typography>
            <LinearProgress variant='determinate' value={60} sx={{height: 10}}/>

            <EditModal/>
            <DeleteModal/>


            <Typography variant="body1" color="textSecondary" component="p">
                Recycled for 6 months
            </Typography>
            <LinearProgress variant='determinate' value={60} sx={{height: 10}}/>

            <EditModal/>
            <DeleteModal/>


            <Typography variant="body1" color="textSecondary" component="p">
                Composted for a week
            </Typography>
            <LinearProgress variant='determinate' value={60} sx={{height: 10}}/>

            <EditModal/>
            <DeleteModal/>

                  
            <IconButton 
                sx={{ color:'grey', transform: 'translate(135px,30px)' }}
                >
                <AddIcon/>
            </IconButton>

            </CardContent>


      </Card>
    </Grid>

        </>
    )
}

export default EditActivityPage;
/*
Minor Details:
1.there's a white area (box) behind Recorder Recycling Efforts, 
  no idea what's that about.
2. Modify box to darker color (black?) when changed to dark mode done  
*/