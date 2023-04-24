import React from 'react';
import { styled, Typography, ListItem, ListItemAvatar, ListItemText} from '@mui/material';
import { AccountCircle } from '@mui/icons-material';

const CustomListItemText = styled(ListItemText)(({ theme }) => ({
  color: theme.palette.surface.text,
}
));

const CustomAccountCircle = styled(AccountCircle)(({ theme }) => ({
  color: theme.palette.surface.text,
}));
function Post(props) {
  return (
    <ListItem>
      <ListItemAvatar><CustomAccountCircle/></ListItemAvatar>
      <CustomListItemText primary={props.title} secundary={props.content}/>
    </ListItem>
  );
}

export default Post;