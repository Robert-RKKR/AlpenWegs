import React, { useEffect, useState } from "react";
import { Table, Input, Button, Space, message } from "antd";
import type { ColumnsType } from "antd/es/table";
import axios from "axios";

interface HikingRoute {
  pk: string;
  name: string;
  snippet: string;
  category: number;
  created: string;
  updated: string;
}

interface ApiResponse {
  page_status: boolean;
  page_results: HikingRoute[];
  page_objects: number;
  page_count: number;
  page_links: {
    page_next: string | null;
    page_previous: string | null;
  };
  page_error: string | null;
}

export default function HikingPage() {
  const [routes, setRoutes] = useState<HikingRoute[]>([]);
  const [loading, setLoading] = useState(false);
  const [searchText, setSearchText] = useState("");
  const [pageUrl, setPageUrl] = useState(
    "http://5.180.148.151:8000/api/explorers/section/"
  );
  const [pagination, setPagination] = useState({
    current: 1,
    pageSize: 10,
    total: 0,
  });

  // Fetch token from localStorage
  const token = localStorage.getItem("access");

  const fetchData = async (url: string, page: number = 1) => {
    if (!token) {
      message.error("Please login first!");
      return;
    }

    setLoading(true);
    try {
      const response = await axios.get<ApiResponse>(url, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });

      const data = response.data;

      if (data.page_status) {
        let results = data.page_results;

        // Apply filter client-side
        if (searchText) {
          results = results.filter((item) =>
            item.name.toLowerCase().includes(searchText.toLowerCase())
          );
        }

        setRoutes(results);
        setPagination({
          current: page,
          pageSize: 10,
          total: data.page_objects, // from API
        });
        setPageUrl(url);
      } else {
        message.error("Failed to load data from API.");
      }
    } catch (err) {
      console.error(err);
      message.error("Error fetching hiking routes.");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchData(pageUrl, 1);
  }, [searchText]);

  const handleTableChange = (pagination: any) => {
    const nextPage = pagination.current;
    const newUrl = `http://5.180.148.151:8000/api/explorers/section/?page_number=${nextPage}`;
    fetchData(newUrl, nextPage);
  };

  const columns: ColumnsType<HikingRoute> = [
    {
      title: "Name",
      dataIndex: "name",
      key: "name",
    },
    {
      title: "Snippet",
      dataIndex: "snippet",
      key: "snippet",
      ellipsis: true,
    },
    {
      title: "Category",
      dataIndex: "category",
      key: "category",
    },
    {
      title: "Created",
      dataIndex: "created",
      key: "created",
      render: (val) => new Date(val).toLocaleDateString(),
    },
    {
      title: "Updated",
      dataIndex: "updated",
      key: "updated",
      render: (val) => new Date(val).toLocaleDateString(),
    },
  ];

  return (
    <div>
      <Space style={{ marginBottom: 16 }}>
        <Input.Search
          placeholder="Search by name"
          allowClear
          enterButton="Search"
          onSearch={(val) => setSearchText(val)}
          style={{ width: 300 }}
        />
        <Button onClick={() => fetchData("http://5.180.148.151:8000/api/explorers/section/", 1)}>
          Reset
        </Button>
      </Space>

      <Table<HikingRoute>
        rowKey="pk"
        loading={loading}
        columns={columns}
        dataSource={routes}
        pagination={pagination}
        onChange={handleTableChange}
      />
    </div>
  );
}
