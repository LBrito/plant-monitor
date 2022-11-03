import React from 'react';
import './App.css';

import 'bootstrap/dist/css/bootstrap.min.css';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col'
import Button from 'react-bootstrap/Button';

import Sensors from './components/sensorData';
import SensorChart from './components/sensorChart';

import { Amplify, Auth } from 'aws-amplify';
import { withAuthenticator } from '@aws-amplify/ui-react';
import '@aws-amplify/ui-react/styles.css';

import awsExports from './aws-exports';

Amplify.configure(awsExports);
Auth.currentCredentials().then(creds => console.log(creds));

function App({ signOut, user }) {
  return (
    <div className="App">
      <Container>
        <Row className="p3 justify-content-md-center">
          <Col className='fs-3 text-start'>Hello {user.username}!</Col>
          <Col className="text-end">
            <Button variant="warning" onClick={signOut}>Sign out</Button>
          </Col>
        </Row>
      </Container>
      <Container>
        <Row className="p-3 justify-content-md-center">
          <Col md="auto"> <Sensors name="relativeTemperature" title="Relative Temperature" unit="°C" /> </Col>
          <Col md="auto"> <Sensors name="relativeHumidity" title="Relative Humidity" unit="%" /> </Col>
        </Row>
      </Container>
      <Container>
        <Row>
          <Col>
            <SensorChart />
          </Col>
        </Row>
      </Container>
    </div>
  );
}

export default withAuthenticator(App, true);
