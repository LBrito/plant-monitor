import React from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

import { Amplify, PubSub } from 'aws-amplify';
import { AWSIoTProvider } from '@aws-amplify/pubsub';
import '@aws-amplify/ui-react/styles.css';

Amplify.addPluggable(new AWSIoTProvider({
    aws_pubsub_region: 'us-east-1',
    aws_pubsub_endpoint: 'wss://a3cvprzqqgdyma-ats.iot.us-east-1.amazonaws.com/mqtt'
}));

class SensorChart extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            values: []
        };
    }

    componentDidMount() {
        PubSub.subscribe('metrics').subscribe({
            next: data => {
                try {
                    this.setState({
                        values: [
                            ...this.state.values,
                            data.value
                        ]
                    });
                }
                catch (error) {
                    console.log("Error, are you sending the correct data?");
                }
            },
            error: error => console.error(error),
            close: () => console.log('Done'),
        });
    }


    render() {
        return (
            <div style={{ width: '100%', height: 300 }}>
                <ResponsiveContainer>
                    <LineChart
                        width={500}
                        height={300}
                        data={this.state.values}
                        margin={{
                            top: 5,
                            right: 30,
                            left: 20,
                            bottom: 5,
                        }}
                    >
                        <CartesianGrid strokeDasharray="3 3" />
                        <XAxis dataKey="timestamp" />
                        <YAxis />
                        <Tooltip />
                        <Legend />
                        <Line type="monotone" dataKey="relativeHumidity" stroke="#8884d8" activeDot={{ r: 8 }} />
                        <Line type="monotone" dataKey="relativeTemperature" stroke="#82ca9d" />
                    </LineChart>
                </ResponsiveContainer>
            </div>
        )
    }
}

export default SensorChart;