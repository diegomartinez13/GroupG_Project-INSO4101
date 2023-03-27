import React, { useState } from 'react';
import { NavLink, useNavigate, useLocation } from 'react-router-dom';
import { styled, Box, Button, List, ListItem, ListItemIcon, ListItemText, BottomNavigation, BottomNavigationAction } from '@mui/material';
import { IconButton } from '@mui/material';
import { Menu, HomeOutlined, EventOutlined, AccountCircleOutlined, DeleteOutlined, ForumOutlined, DeleteOutlineOutlined, Home, Event, PersonOutline, Forum, Delete, Person } from '@mui/icons-material';

const SideNavWrapper = styled('div')(({ theme, open }) => ({
  position: 'fixed',
  top: 0,
  bottom: 0,
  left: 0,
  width: open ? '240px' : '56px',
  transition: theme.transitions.create('width', {
    easing: theme.transitions.easing.sharp,
    duration: theme.transitions.duration.standard,
  }),
  backgroundColor: theme.palette.primary.main,
  color: theme.palette.common.white,
}));

const ToggleButton = styled(IconButton)(({ theme }) => ({
  color: theme.palette.common.white,
  '&:hover': {
    backgroundColor: 'rgba(255, 255, 255, 0.08)',
  },
}));

const NavList = styled(List)(({ theme }) => ({
  paddingTop: theme.spacing(6),
}));

const NavListItem = styled(ListItem)(({ theme }) => ({
  '&:hover': {
    backgroundColor: 'rgba(255, 255, 255, 0.08)',
  },
}));

const NavListItemIcon = styled(ListItemIcon)(({ theme }) => ({
  color: theme.palette.common.white,
}));

const NavListItemText = styled(ListItemText)(({ theme }) => ({
  color: theme.palette.common.white,
}));

const BottomNavWrapper = styled(BottomNavigation)(({ theme }) => ({
  position: 'fixed',
  bottom: 0,
  left: 0,
  right: 0,
  backgroundColor: theme.palette.primary.main,
  color: theme.palette.common.white,
}));

const BottomNavAction = styled(BottomNavigationAction)(({ theme }) => ({
  color: theme.palette.common.white,
}));

const SideNavigation = () => {
  const [isOpen, setIsOpen] = useState(false);
  const location = useLocation();
  const navigate = useNavigate();
  const handleNavigation = (path) => {
    navigate(path);
  }

  const handleToggle = () => {
    setIsOpen(!isOpen);
  };
  
  const isMobile = window.innerWidth < 600;

  if (isMobile) {
    return (
      <BottomNavWrapper>
        <BottomNavAction label="Events" icon={<EventOutlined />} component={NavLink} to="/" />
        <BottomNavAction label="Forum" icon={<ForumOutlined />} component={NavLink} to="/forum" />
        <BottomNavAction label="Recycling Centers" icon={<DeleteOutlined />} component={NavLink} to="/recycling-centers" />
        <BottomNavAction label="Profile" icon={<AccountCircleOutlined />} component={NavLink} to="/profile" />
      </BottomNavWrapper>
    );
  }
  return (
    <SideNavWrapper open={isOpen}>
      <ToggleButton onClick={handleToggle}>
        {isOpen ? <Menu /> : <Menu />}
      </ToggleButton>
      <NavList>
        <NavListItem button component={NavLink} to="/" exact activeClassName="Mui-selected">
          <NavListItemIcon>
            {location.pathname === '/' ? <Home /> : <HomeOutlined />}
          </NavListItemIcon>
          <NavListItemText primary="Home" />
        </NavListItem>
        <NavListItem button component={NavLink} to="/events" exact activeClassName="Mui-selected">
          <NavListItemIcon>
            {location.pathname === '/events' ? <Event /> : <EventOutlined />}
          </NavListItemIcon>
          <NavListItemText primary="Events" />
        </NavListItem>
        <NavListItem button component={NavLink} to="/forum" exact activeClassName="Mui-selected">
          <NavListItemIcon>
            {location.pathname === '/forum' ? <Forum /> : <ForumOutlined />}
          </NavListItemIcon>
          <NavListItemText primary="Forum" />
        </NavListItem>
        <NavListItem button component={NavLink} to="/recycling-centers" exact activeClassName="Mui-selected">
          <NavListItemIcon>
            {location.pathname === '/recycling-centers' ? <Delete /> : <DeleteOutlineOutlined />}
          </NavListItemIcon>
          <NavListItemText primary="Recycling Centers" />
        </NavListItem>
        <NavListItem button component={NavLink} to="/profile" exact activeClassName="Mui-selected">
          <NavListItemIcon>
            {location.pathname === '/profile' ? <Person /> : <PersonOutline />}
          </NavListItemIcon>
          <NavListItemText primary="Profile" />
        </NavListItem>
      </NavList>
    </SideNavWrapper>
  );
};

export default SideNavigation;