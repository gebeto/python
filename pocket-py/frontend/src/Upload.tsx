import React from 'react';

import { FileUploader } from "baseui/file-uploader";


export const Upload = () => {
	const [errorMessage, setErrorMessage] = React.useState("");

	return <FileUploader errorMessage={errorMessage} />;
}