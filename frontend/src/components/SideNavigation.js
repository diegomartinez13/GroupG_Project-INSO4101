import React, { useState } from 'react';
import { NavLink, useLocation } from 'react-router-dom';
import { styled, List, ListItem, ListItemIcon, ListItemText, BottomNavigation, BottomNavigationAction, useMediaQuery } from '@mui/material';
import { IconButton } from '@mui/material';
import { Menu, AccountCircle, HomeOutlined, EventOutlined, AccountCircleOutlined, ForumOutlined, Home, Event, PersonOutline, Forum, Person, Map, MapOutlined } from '@mui/icons-material';

const SideNavWrapper = styled('div')(({ theme, open }) => ({
  position: 'fixed',
  top: 0,
  bottom: 0,
  left: 0,
  zIndex: 1,
  width: open ? '16em' : '4em',
  transition: theme.transitions.create('width', {
    easing: theme.transitions.easing.sharp,
    duration: theme.transitions.duration.standard,
  }),
  backgroundColor: theme.palette.surface.main,
  color: theme.palette.common.white,
}));

const ToggleButton = styled(IconButton)(({ theme }) => ({
  color: theme.palette.surface.onVariant,
  alignContent: 'center',
  justifyContent: 'center',
  marginLeft: '0.5em',
  '&:hover': {
    backgroundColor: theme.palette.secondary.container.main,
  },
}));

const NavList = styled(List)(({ theme }) => ({
  paddingTop: theme.spacing(6),
  marginRight: theme.spacing(0.5),
  marginLeft: theme.spacing(0.5),
}));

const NavListItem = styled(ListItem)(({ theme }) => ({
  color: theme.palette.surface.onVariant,
  '&:hover': {
    backgroundColor: theme.palette.secondary.container.main,
    // Round the corners of the list item
    borderRadius: '0.8rem',
    color: theme.palette.secondary.container.onContainer,
    text: theme.palette.secondary.container.onContainerText,

  },
}));

const NavListItemIcon = styled(ListItemIcon)(({ theme }) => ({
  color: theme.palette.surface.onVariant,
}));

const NavListItemText = styled(ListItemText)(({ theme }) => ({
  color: theme.palette.surface.onVariant,
}));

const BottomNavWrapper = styled(BottomNavigation)(({ theme }) => ({
  position: 'fixed',
  bottom: 0,
  left: 0,
  right: 0,
  backgroundColor: theme.palette.surface.main,
  color: theme.palette.surface.onVariant,

}));

const BottomNavAction = styled(BottomNavigationAction)(({ theme }) => ({
  color: theme.palette.surface.onVariant,
  minWidth: 0,
  margin: '0.5rem',
  padding: theme.spacing(1),
  '& .MuiBottomNavigationAction-iconOnly': {
    fontSize: '1.2rem',
  },
  '& .MuiSvgIcon-root': {
    fontSize: '1.5rem',
  },
  '@media (max-width: 600px)': {
    '& .MuiBottomNavigationAction-iconOnly': {
      fontSize: '1rem',
    },
    '& .MuiSvgIcon-root': {
      fontSize: '1.2rem',
    },
  },
  '&:hover': {
    backgroundColor: theme.palette.secondary.container.main,
    color: theme.palette.secondary.container.onContainer,
    text: theme.palette.secondary.container.onContainerText,
    borderRadius: '0.8rem',
  },
}));

function SideNavigation({ onToggleMenu }) {
  const [isOpen, setIsOpen] = useState(false);
  const location = useLocation();
  

  const handleToggle = () => {
    setIsOpen(!isOpen);
    onToggleMenu();
  };
  
  const isSmallScreen = useMediaQuery('(max-width:600px)');

  if (isSmallScreen) {
    return (
      <BottomNavWrapper>
        <BottomNavAction showLabel={true} label="Home" icon={location.pathname === '/' ? <Home /> : <HomeOutlined />} component={NavLink} to="/" />
        <BottomNavAction showLabel={true} label="Events" icon={location.pathname === '/events' ? <Event /> : <EventOutlined />} component={NavLink} to="/events" />
        <BottomNavAction showLabel={true} label="Forum" icon={location.pathname === '/forum' ? <Forum /> : <ForumOutlined />} component={NavLink} to="/forum" />
        <BottomNavAction showLabel={true} label="Map" icon={location.pathname === '/recycling-centers' ? <Map /> : <MapOutlined />} component={NavLink} to="/recycling-centers" />
        <BottomNavAction showLabel={true} label="Profile" icon={location.pathname === '/profile' ? <AccountCircle /> : <AccountCircleOutlined />} component={NavLink} to="/profile" />
      </BottomNavWrapper>
    );
  }
  return (
    <SideNavWrapper open={isOpen}>
      <ToggleButton onClick={handleToggle}>
        {isOpen ? <Menu /> : <Menu />}
      </ToggleButton>
      <NavList>
        <NavListItem button component={NavLink} to="/"  >
          <NavListItemIcon>
            {location.pathname === '/' ? <Home /> : <HomeOutlined />}
          </NavListItemIcon>
          <NavListItemText primary={isOpen ? "Home" : ""} />
        </NavListItem>
        <NavListItem button component={NavLink} to="/events"  >
          <NavListItemIcon>
            {location.pathname === '/events' ? <Event /> : <EventOutlined />}
          </NavListItemIcon>
          <NavListItemText primary={isOpen ? "Events" : ""} />
        </NavListItem>
        <NavListItem button component={NavLink} to="/forum"  >
          <NavListItemIcon>
            {location.pathname === '/forum' ? <Forum /> : <ForumOutlined />}
          </NavListItemIcon>
          <NavListItemText primary={isOpen ? "Forum" : "" } />
        </NavListItem>
        <NavListItem button component={NavLink} to="/recycling-centers"  >
          <NavListItemIcon>
            {location.pathname === '/recycling-centers' ? <Map /> : <MapOutlined />}
          </NavListItemIcon>
          <NavListItemText primary={isOpen ? "Recycling Centers" : "" } />
        </NavListItem>
        <NavListItem button component={NavLink} to="/profile"  >
          <NavListItemIcon>
            {location.pathname === '/profile' ? <Person /> : <PersonOutline />}
          </NavListItemIcon>
          <NavListItemText primary={isOpen ? "Profile" : "" } />
        </NavListItem>
      </NavList>
    </SideNavWrapper>
  );
};

export default SideNavigation;