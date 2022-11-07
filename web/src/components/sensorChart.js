import React from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, Area, AreaChart } from 'recharts';
import { format } from 'date-fns'
import { Amplify, PubSub } from 'aws-amplify';
import { AWSIoTProvider } from '@aws-amplify/pubsub';
import '@aws-amplify/ui-react/styles.css';

Amplify.addPluggable(new AWSIoTProvider({
    aws_pubsub_region: 'us-east-1',
    aws_pubsub_endpoint: 'wss://a3cvprzqqgdyma-ats.iot.us-east-1.amazonaws.com/mqtt'
}));

const CustomTooltip = ({ active, payload, label }) => {
    if (active && payload && payload.length) {
        console.log(payload)
        return (
            <div style={{ background: "white", height: "100%", border: "1px #b1afaf solid", textAlign: "left", padding: "5px 15px" }}>
                <p className="label" style={{ color: payload[0].stroke }}>
                    {`${payload[0].dataKey} : ${Math.round((payload[0].value || 0) * 100) / 100} %`}
                </p>
                <p className="label" style={{ color: payload[1].stroke }}>
                    {`${payload[1].dataKey} : ${Math.round((payload[1].value || 0) * 100) / 100} °C`}
                </p>
                <p className="desc" style={{ textAlign: "center", color: "#5e5e5e" }}>{`${format(new Date(label), 'yyyy/MM/dd HH:mm:ss')}`}</p>
            </div>
        );
    }

    return null;
};
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
                    <AreaChart
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
                        <defs>
                            <linearGradient id="colorA" x1="0" y1="0" x2="0" y2="1">
                                <stop offset="5%" stopColor="#5e9ce6" stopOpacity={0.8} />
                                <stop offset="95%" stopColor="#5e9ce6" stopOpacity={0} />
                            </linearGradient>
                            <linearGradient id="colorB" x1="0" y1="0" x2="0" y2="1">
                                <stop offset="5%" stopColor="#82ca9d" stopOpacity={0.8} />
                                <stop offset="95%" stopColor="#82ca9d" stopOpacity={0} />
                            </linearGradient>
                        </defs>

                        <CartesianGrid strokeDasharray="3 3" />
                        <XAxis dataKey="timestamp" />
                        <YAxis />
                        <Tooltip content={<CustomTooltip />} />
                        <Legend />
                        <Area type="monotone" dataKey="relativeHumidity" stroke="#5e9ce6" fillOpacity={1} fill="url(#colorA)" />
                        <Area type="monotone" dataKey="relativeTemperature" stroke="#82ca9d" fillOpacity={1} fill="url(#colorB)" />
                    </AreaChart>
                </ResponsiveContainer>
            </div>
        )
    }
}

export default SensorChart;