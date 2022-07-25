import React from 'react'

import Dialog from '@mui/material/Dialog';
import Slide from '@mui/material/Slide';

const Transition = React.forwardRef(function Transition(props, ref) {
  return <Slide direction="up" ref={ref} {...props} />;
});

const VideoFrame = (props) => {
  const vid = props.url
  const getYouTubeId = require('get-youtube-id')
  const id = getYouTubeId(vid)

  return (
    <div>
      {/* <Button variant="outlined" onClick={() => props.handleClickOpen()}>
        Slide in alert dialog
      </Button> */}
      <Dialog
        open={props.openState}
        fullWidth={true}
        maxWidth='xl'
        TransitionComponent={Transition}
        keepMounted
        onClose={props.handleClose}
        aria-describedby="alert-dialog-slide-description"
      > 
        <iframe
          style={{
            width: '100%',
            aspectRatio: 4 / 1.7,
          }}
          src={`https://www.youtube.com/embed/${id}`}
          frameborder="0"
          allow="accelerometer; autoplay; encrypted-media; gyroscope;"
          allowfullscreen>  
        </iframe>
      </Dialog>
    </div>
  )
}

export default VideoFrame