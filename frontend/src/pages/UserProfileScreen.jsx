import React from 'react';
import { useNavigate } from 'react-router-dom';
import NavigationBarHome from '../components/NavigationBarHome';

export default function UserProfileScreen () {
  const navigate = useNavigate();
  return (
  <div>
    <NavigationBarHome style={{ alignSelf: 'start' }} isLogin={true} ></NavigationBarHome>
    <h2 style={{ maxWidth: '100%' }}>
      PUBLIC USER PROFILE SCREEN COMING SOON!
    </h2>
  </div>
  )
}