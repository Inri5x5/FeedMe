import React from 'react';
import { useNavigate } from 'react-router-dom';
import NavigationBarHome from '../components/NavigationBarHome';
import LeftNavDashboard from '../components/LeftNavDashboard';
import RecipeDashboard from '../components/RecipeDashboard';

export default function UserProfileScreen () {
  const navigate = useNavigate();
  const [clickedButton, setClickedButton] = React.useState('')
  
  React.useEffect(() => {
    //Fetch the recipe
  }, [clickedButton])
  
  return (
    <>
      <div style={{ 
        display:'flex',
        flexDirection:'column',
        height: '100%',
        minHeight: 0,
        overflow: 'hidden'
      }}>
        <NavigationBarHome style={{ alignSelf: 'start', flex: 1 }} isLogin={true} ></NavigationBarHome>
        <div style={{
          display:'flex',
          flexDirection:'row',
          flex: 4,
          height: '100%'
        }}>
          <LeftNavDashboard
            clickedButton={clickedButton}
            setClickedButton={setClickedButton} 
          />
          <RecipeDashboard
            clickedButton={clickedButton} 
          />
        </div>
      </div>
    </>
  )
}