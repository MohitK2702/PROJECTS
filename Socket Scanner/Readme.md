<p>You can add several additional functionalities to enhance the port scanner's capabilities, making it more versatile and efficient. Here are a few features that can be added:</p><h3>1. <strong>Service Detection</strong></h3><ul><li><strong>Functionality</strong>: Display the service running on each open port (e.g., HTTP for port 80, SSH for port 22).</li><li><strong>Implementation</strong>: Use a dictionary to map common port numbers to services. Optionally, you can integrate libraries like <code>scapy</code> or <code>socket.getservbyport()</code> for more dynamic detection.</li></ul><p><strong>Code Snippet:</strong></p><pre class="!overflow-visible"><div class="dark bg-gray-950 contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative"><div class="flex items-center text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md h-9">python</div><div class="sticky top-9 md:top-[5.75rem]"><div class="absolute bottom-0 right-2 flex h-9 items-center"><div class="flex items-center rounded bg-token-main-surface-secondary px-2 font-sans text-xs text-token-text-secondary"><span class="" data-state="closed"><button class="flex gap-1 items-center py-1"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"><path fill-rule="evenodd" clip-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg> </button></span></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-python"><span class="hljs-comment"># Add this function to map ports to services</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">get_service</span>(<span class="hljs-params">port</span>):
    <span class="hljs-keyword">try</span>:
        <span class="hljs-keyword">return</span> socket.getservbyport(port)
    <span class="hljs-keyword">except</span>:
        <span class="hljs-keyword">return</span> <span class="hljs-string">"Unknown service"</span>

<span class="hljs-comment"># Modify scan_port function to include service detection</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">scan_port</span>(<span class="hljs-params">ip, port</span>):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(<span class="hljs-number">1</span>)
    <span class="hljs-keyword">try</span>:
        result = scanner.connect_ex((ip, port))
        <span class="hljs-keyword">if</span> result == <span class="hljs-number">0</span>:
            service = get_service(port)
            <span class="hljs-built_in">print</span>(<span class="hljs-string">f"Port <span class="hljs-subst">{port}</span> is open (<span class="hljs-subst">{service}</span>)"</span>)
        scanner.close()
    <span class="hljs-keyword">except</span> Exception <span class="hljs-keyword">as</span> e:
        <span class="hljs-built_in">print</span>(<span class="hljs-string">f"Error scanning port <span class="hljs-subst">{port}</span>: <span class="hljs-subst">{<span class="hljs-built_in">str</span>(e)}</span>"</span>)
</code></div></div></pre><h3>2. <strong>Range and Common Port Presets</strong></h3><ul><li><strong>Functionality</strong>: Instead of asking for a port range, provide options to scan:<ul><li><strong>All ports</strong> (1-65535)</li><li><strong>Common ports</strong> (HTTP, FTP, SSH, DNS, etc.)</li></ul></li><li><strong>Implementation</strong>: Predefine common port lists and allow the user to select options.</li></ul><p><strong>Code Snippet:</strong></p><pre class="!overflow-visible"><div class="dark bg-gray-950 contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative"><div class="flex items-center text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md h-9">python</div><div class="sticky top-9 md:top-[5.75rem]"><div class="absolute bottom-0 right-2 flex h-9 items-center"><div class="flex items-center rounded bg-token-main-surface-secondary px-2 font-sans text-xs text-token-text-secondary"><span class="" data-state="closed"><button class="flex gap-1 items-center py-1"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"><path fill-rule="evenodd" clip-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg> </button></span></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-python"><span class="hljs-comment"># Common ports for popular services</span>
common_ports = {
    <span class="hljs-string">"FTP"</span>: <span class="hljs-number">21</span>,
    <span class="hljs-string">"SSH"</span>: <span class="hljs-number">22</span>,
    <span class="hljs-string">"Telnet"</span>: <span class="hljs-number">23</span>,
    <span class="hljs-string">"HTTP"</span>: <span class="hljs-number">80</span>,
    <span class="hljs-string">"HTTPS"</span>: <span class="hljs-number">443</span>,
    <span class="hljs-string">"DNS"</span>: <span class="hljs-number">53</span>
}

<span class="hljs-keyword">def</span> <span class="hljs-title function_">scan_common_ports</span>(<span class="hljs-params">ip</span>):
    <span class="hljs-keyword">for</span> service, port <span class="hljs-keyword">in</span> common_ports.items():
        thread = threading.Thread(target=scan_port, args=(ip, port))
        thread.start()

<span class="hljs-comment"># Modify main function to include option for scanning common ports</span>
<span class="hljs-keyword">if</span> __name__ == <span class="hljs-string">"__main__"</span>:
    target_ip = <span class="hljs-built_in">input</span>(<span class="hljs-string">"Enter the IP address to scan: "</span>)
    scan_type = <span class="hljs-built_in">input</span>(<span class="hljs-string">"Choose scan type: [1] Full range (1-65535), [2] Common ports: "</span>)
    
    <span class="hljs-keyword">if</span> scan_type == <span class="hljs-string">"1"</span>:
        scan_ports(target_ip, <span class="hljs-number">1</span>, <span class="hljs-number">65535</span>)
    <span class="hljs-keyword">elif</span> scan_type == <span class="hljs-string">"2"</span>:
        scan_common_ports(target_ip)
</code></div></div></pre><h3>3. <strong>Banner Grabbing</strong></h3><ul><li><strong>Functionality</strong>: Capture banners from open ports, which can provide version information about services and reveal potential vulnerabilities.</li><li><strong>Implementation</strong>: After detecting an open port, attempt to retrieve the service banner.</li></ul><p><strong>Code Snippet:</strong></p><pre class="!overflow-visible"><div class="dark bg-gray-950 contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative"><div class="flex items-center text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md h-9">python</div><div class="sticky top-9 md:top-[5.75rem]"><div class="absolute bottom-0 right-2 flex h-9 items-center"><div class="flex items-center rounded bg-token-main-surface-secondary px-2 font-sans text-xs text-token-text-secondary"><span class="" data-state="closed"><button class="flex gap-1 items-center py-1"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"><path fill-rule="evenodd" clip-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg> </button></span></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-python"><span class="hljs-keyword">def</span> <span class="hljs-title function_">grab_banner</span>(<span class="hljs-params">ip, port</span>):
    <span class="hljs-keyword">try</span>:
        s = socket.socket()
        s.connect((ip, port))
        s.send(<span class="hljs-string">b'HEAD / HTTP/1.1\r\n\r\n'</span>)
        banner = s.recv(<span class="hljs-number">1024</span>)
        <span class="hljs-keyword">return</span> banner.decode().strip()
    <span class="hljs-keyword">except</span> Exception <span class="hljs-keyword">as</span> e:
        <span class="hljs-keyword">return</span> <span class="hljs-string">"No banner"</span>

<span class="hljs-comment"># Modify scan_port function to include banner grabbing</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">scan_port</span>(<span class="hljs-params">ip, port</span>):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(<span class="hljs-number">1</span>)
    <span class="hljs-keyword">try</span>:
        result = scanner.connect_ex((ip, port))
        <span class="hljs-keyword">if</span> result == <span class="hljs-number">0</span>:
            service = get_service(port)
            banner = grab_banner(ip, port)
            <span class="hljs-built_in">print</span>(<span class="hljs-string">f"Port <span class="hljs-subst">{port}</span> is open (<span class="hljs-subst">{service}</span>) - Banner: <span class="hljs-subst">{banner}</span>"</span>)
        scanner.close()
    <span class="hljs-keyword">except</span> Exception <span class="hljs-keyword">as</span> e:
        <span class="hljs-built_in">print</span>(<span class="hljs-string">f"Error scanning port <span class="hljs-subst">{port}</span>: <span class="hljs-subst">{<span class="hljs-built_in">str</span>(e)}</span>"</span>)
</code></div></div></pre><h3>4. <strong>Logging to a File</strong></h3><ul><li><strong>Functionality</strong>: Save the scanning results to a text or CSV file for future reference.</li><li><strong>Implementation</strong>: Append results to a file as they are found, allowing for easier tracking and auditing.</li></ul><p><strong>Code Snippet:</strong></p><pre class="!overflow-visible"><div class="dark bg-gray-950 contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative"><div class="flex items-center text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md h-9">python</div><div class="sticky top-9 md:top-[5.75rem]"><div class="absolute bottom-0 right-2 flex h-9 items-center"><div class="flex items-center rounded bg-token-main-surface-secondary px-2 font-sans text-xs text-token-text-secondary"><span class="" data-state="closed"><button class="flex gap-1 items-center py-1"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"><path fill-rule="evenodd" clip-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg> </button></span></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-python"><span class="hljs-keyword">import</span> csv

<span class="hljs-comment"># Add a function to log results to a CSV file</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">log_to_file</span>(<span class="hljs-params">ip, port, service, banner</span>):
    <span class="hljs-keyword">with</span> <span class="hljs-built_in">open</span>(<span class="hljs-string">'scan_results.csv'</span>, mode=<span class="hljs-string">'a'</span>, newline=<span class="hljs-string">''</span>) <span class="hljs-keyword">as</span> file:
        writer = csv.writer(file)
        writer.writerow([ip, port, service, banner])

<span class="hljs-comment"># Modify scan_port function to include logging</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">scan_port</span>(<span class="hljs-params">ip, port</span>):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(<span class="hljs-number">1</span>)
    <span class="hljs-keyword">try</span>:
        result = scanner.connect_ex((ip, port))
        <span class="hljs-keyword">if</span> result == <span class="hljs-number">0</span>:
            service = get_service(port)
            banner = grab_banner(ip, port)
            <span class="hljs-built_in">print</span>(<span class="hljs-string">f"Port <span class="hljs-subst">{port}</span> is open (<span class="hljs-subst">{service}</span>) - Banner: <span class="hljs-subst">{banner}</span>"</span>)
            log_to_file(ip, port, service, banner)  <span class="hljs-comment"># Logging result</span>
        scanner.close()
    <span class="hljs-keyword">except</span> Exception <span class="hljs-keyword">as</span> e:
        <span class="hljs-built_in">print</span>(<span class="hljs-string">f"Error scanning port <span class="hljs-subst">{port}</span>: <span class="hljs-subst">{<span class="hljs-built_in">str</span>(e)}</span>"</span>)
</code></div></div></pre><h3>5. <strong>IP Range Scanning (Subnet Scanning)</strong></h3><ul><li><strong>Functionality</strong>: Allow scanning of an entire subnet (e.g., 192.168.1.0/24) instead of just a single IP.</li><li><strong>Implementation</strong>: Use a library like <code>ipaddress</code> to handle subnet scanning.</li></ul><p><strong>Code Snippet:</strong></p><pre class="!overflow-visible"><div class="dark bg-gray-950 contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative"><div class="flex items-center text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md h-9">python</div><div class="sticky top-9 md:top-[5.75rem]"><div class="absolute bottom-0 right-2 flex h-9 items-center"><div class="flex items-center rounded bg-token-main-surface-secondary px-2 font-sans text-xs text-token-text-secondary"><span class="" data-state="closed"><button class="flex gap-1 items-center py-1"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"><path fill-rule="evenodd" clip-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg> </button></span></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-python"><span class="hljs-keyword">import</span> ipaddress

<span class="hljs-comment"># Function to scan an IP range</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">scan_ip_range</span>(<span class="hljs-params">network</span>):
    net = ipaddress.ip_network(network)
    <span class="hljs-keyword">for</span> ip <span class="hljs-keyword">in</span> net.hosts():
        <span class="hljs-built_in">print</span>(<span class="hljs-string">f"\nScanning IP: <span class="hljs-subst">{ip}</span>"</span>)
        scan_ports(<span class="hljs-built_in">str</span>(ip), <span class="hljs-number">1</span>, <span class="hljs-number">1024</span>)  <span class="hljs-comment"># Scan first 1024 ports for each IP</span>

<span class="hljs-keyword">if</span> __name__ == <span class="hljs-string">"__main__"</span>:
    scan_type = <span class="hljs-built_in">input</span>(<span class="hljs-string">"Scan single IP (1) or subnet (2): "</span>)
    <span class="hljs-keyword">if</span> scan_type == <span class="hljs-string">"2"</span>:
        subnet = <span class="hljs-built_in">input</span>(<span class="hljs-string">"Enter the subnet (e.g., 192.168.1.0/24): "</span>)
        scan_ip_range(subnet)
    <span class="hljs-keyword">else</span>:
        target_ip = <span class="hljs-built_in">input</span>(<span class="hljs-string">"Enter the IP address to scan: "</span>)
        scan_ports(target_ip, <span class="hljs-number">1</span>, <span class="hljs-number">1024</span>)
</code></div></div></pre><h3>6. <strong>Multi-threading Improvements (Thread Pool)</strong></h3><ul><li><strong>Functionality</strong>: Use a thread pool to limit the number of threads running simultaneously, improving performance and reducing resource consumption.</li><li><strong>Implementation</strong>: Use <code>concurrent.futures</code> to manage the thread pool efficiently.</li></ul><p><strong>Code Snippet:</strong></p><pre class="!overflow-visible"><div class="dark bg-gray-950 contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative"><div class="flex items-center text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md h-9">python</div><div class="sticky top-9 md:top-[5.75rem]"><div class="absolute bottom-0 right-2 flex h-9 items-center"><div class="flex items-center rounded bg-token-main-surface-secondary px-2 font-sans text-xs text-token-text-secondary"><span class="" data-state="closed"><button class="flex gap-1 items-center py-1"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"><path fill-rule="evenodd" clip-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg> </button></span></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-python"><span class="hljs-keyword">from</span> concurrent.futures <span class="hljs-keyword">import</span> ThreadPoolExecutor

<span class="hljs-keyword">def</span> <span class="hljs-title function_">scan_ports_with_pool</span>(<span class="hljs-params">ip, start_port, end_port, max_threads=<span class="hljs-number">100</span></span>):
    <span class="hljs-keyword">with</span> ThreadPoolExecutor(max_workers=max_threads) <span class="hljs-keyword">as</span> executor:
        <span class="hljs-keyword">for</span> port <span class="hljs-keyword">in</span> <span class="hljs-built_in">range</span>(start_port, end_port + <span class="hljs-number">1</span>):
            executor.submit(scan_port, ip, port)

<span class="hljs-keyword">if</span> __name__ == <span class="hljs-string">"__main__"</span>:
    target_ip = <span class="hljs-built_in">input</span>(<span class="hljs-string">"Enter the IP address to scan: "</span>)
    start_port = <span class="hljs-built_in">int</span>(<span class="hljs-built_in">input</span>(<span class="hljs-string">"Enter the start port: "</span>))
    end_port = <span class="hljs-built_in">int</span>(<span class="hljs-built_in">input</span>(<span class="hljs-string">"Enter the end port: "</span>))
    
    <span class="hljs-comment"># Using thread pool to manage threads efficiently</span>
    scan_ports_with_pool(target_ip, start_port, end_port)
</code></div></div></pre><h3>7. <strong>OS Detection</strong></h3><ul><li><strong>Functionality</strong>: Attempt to determine the operating system of the target machine.</li><li><strong>Implementation</strong>: This can be complex and would generally require integration with a more advanced library like <code>scapy</code> or using specific flags in TCP packets (e.g., OS fingerprinting techniques).</li></ul><h3>8. <strong>Email Notifications or Alerts</strong></h3><ul><li><strong>Functionality</strong>: Send an email alert when open ports are detected or when a scan completes.</li><li><strong>Implementation</strong>: Use libraries like <code>smtplib</code> to send emails with the results.</li></ul><p><strong>Code Snippet:</strong></p><pre class="!overflow-visible"><div class="dark bg-gray-950 contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative"><div class="flex items-center text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md h-9">python</div><div class="sticky top-9 md:top-[5.75rem]"><div class="absolute bottom-0 right-2 flex h-9 items-center"><div class="flex items-center rounded bg-token-main-surface-secondary px-2 font-sans text-xs text-token-text-secondary"><span class="" data-state="closed"><button class="flex gap-1 items-center py-1"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"><path fill-rule="evenodd" clip-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg> </button></span></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-python"><span class="hljs-keyword">import</span> smtplib
<span class="hljs-keyword">from</span> email.mime.text <span class="hljs-keyword">import</span> MIMEText

<span class="hljs-keyword">def</span> <span class="hljs-title function_">send_email</span>(<span class="hljs-params">subject, body</span>):
    sender = <span class="hljs-string">"your_email@example.com"</span>
    receiver = <span class="hljs-string">"receiver_email@example.com"</span>
    msg = MIMEText(body)
    msg[<span class="hljs-string">'Subject'</span>] = subject
    msg[<span class="hljs-string">'From'</span>] = sender
    msg[<span class="hljs-string">'To'</span>] = receiver
    
    <span class="hljs-keyword">with</span> smtplib.SMTP(<span class="hljs-string">"smtp.example.com"</span>, <span class="hljs-number">587</span>) <span class="hljs-keyword">as</span> server:
        server.starttls()
        server.login(sender, <span class="hljs-string">"password"</span>)
        server.sendmail(sender, receiver, msg.as_string())

<span class="hljs-comment"># Call send_email function after scanning</span>
<span class="hljs-keyword">if</span> __name__ == <span class="hljs-string">"__main__"</span>:
    <span class="hljs-comment"># ... after scan finishes</span>
    send_email(<span class="hljs-string">"Port Scan Complete"</span>, <span class="hljs-string">"The scan results are ..."</span>)
</code></div></div></pre><h3>9. <strong>Geolocation of IP Address</strong></h3><ul><li><strong>Functionality</strong>: Show the geographic location of the target IP address (using a public IP).</li><li><strong>Implementation</strong>: Use a service like <code>ipinfo.io</code> to fetch geolocation data.</li></ul><p>These are some enhancements that could turn the basic scanner into a more advanced and useful security tool. </p>
