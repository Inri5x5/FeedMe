import React from 'react'

import Slide from '@mui/material/Slide';

const Transition = React.forwardRef(function Transition(props, ref) {
  return <Slide direction="up" ref={ref} {...props} />;
});

const RecipeVideo = (props) => {
  const vid = props.url
  const getYouTubeId = require('get-youtube-id')
  const id = getYouTubeId(vid)

  return (
    <div>
        <iframe
          style={{
            width: '100%',
            aspectRatio: 4 / 1.7,
          }}
          src={`https://www.youtube.com/embed/${id}`}
          frameBorder="0"
          allow="accelerometer; autoplay; encrypted-media; gyroscope;"
          allowFullScreen>  
        </iframe>
    </div>
  )
}

export default RecipeVideo